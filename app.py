import os
import sys
import joblib
import pandas as pd
from flask import Flask, render_template, request, jsonify

# Vérifier la version de Python
if sys.version_info < (3, 9):
    print("=" * 60)
    print("❌ ERREUR: Python 3.9 ou supérieur est requis!")
    print("=" * 60)
    print(f"Version Python actuelle: {sys.version}")
    print("\nLe modèle nécessite numpy 2.x qui requiert Python 3.9+")
    print("\nSolutions:")
    print("1. Mettez à jour Python vers 3.9 ou supérieur")
    print("2. Ou réentraînez le modèle avec numpy 1.x")
    print("=" * 60)
    sys.exit(1)

# Afficher la version Python pour vérification
print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} détecté")

app = Flask(__name__)

# Charger le modèle au démarrage
MODEL_PATH = 'laptop_price_model_v2.pkl'
model = None

def load_model():
    """Charge le modèle de prédiction"""
    import warnings
    global model
    if model is None:
        try:
            # Ignorer les warnings de version sklearn lors du chargement
            with warnings.catch_warnings():
                warnings.filterwarnings('ignore', category=UserWarning)
                model = joblib.load(MODEL_PATH)
            print(f"✅ Modèle chargé avec succès depuis {MODEL_PATH}")
        except FileNotFoundError:
            print(f"❌ Erreur: Le fichier {MODEL_PATH} n'a pas été trouvé")
            print("   Veuillez vous assurer que le fichier laptop_price_model_v2.pkl existe")
            raise
        except Exception as e:
            print(f"❌ Erreur lors du chargement du modèle: {str(e)}")
            raise
    return model

# Charger le modèle au démarrage
try:
    load_model()
except:
    print("⚠️  Le modèle ne sera pas chargé au démarrage. Vérifiez le fichier.")

@app.route('/')
def index():
    """Page d'accueil"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint pour la prédiction du prix"""
    try:
        if model is None:
            return jsonify({
                'error': 'Le modèle n\'est pas chargé. Vérifiez que laptop_price_model_v2.pkl existe.'
            }), 500
        
        # Récupérer les données du formulaire
        data = request.get_json()
        
        # Vérifier que tous les champs requis sont remplis
        required_fields = ['Company', 'TypeName', 'CPU_Type', 'RAM', 'Memory', 'GPU_Type', 'Inches']
        for field in required_fields:
            if not data.get(field, ''):
                return jsonify({
                    'error': f'Le champ {field} est requis'
                }), 400
        
        # Construire les données pour le modèle
        laptop_data = {
            'Company': str(data.get('Company', '')).strip(),
            'TypeName': str(data.get('TypeName', '')).strip(),
            'Inches': float(data.get('Inches', 0)),
            'ScreenResolution': str(data.get('ScreenResolution', '')).strip(),
            'CPU_Company': str(data.get('CPU_Company', 'Intel')).strip(),
            'CPU_Type': str(data.get('CPU_Type', '')).strip(),
            'CPU_Frequency (GHz)': float(data.get('CPU_Frequency', 2.0)),
            'RAM (GB)': int(data.get('RAM', 0)),
            'Memory': str(data.get('Memory', '')).strip(),
            'GPU_Company': str(data.get('GPU_Company', 'Intel')).strip(),
            'GPU_Type': str(data.get('GPU_Type', '')).strip(),
            'OpSys': str(data.get('OpSys', 'Windows')).strip(),
            'Weight (kg)': float(data.get('Weight', 2.0))
        }
        
        # Vérifier les valeurs numériques
        if laptop_data['Inches'] <= 0:
            return jsonify({'error': 'La taille d\'écran (Inches) doit être supérieure à 0'}), 400
        if laptop_data['RAM (GB)'] <= 0:
            return jsonify({'error': 'La RAM doit être supérieure à 0'}), 400
        
        # Convertir en DataFrame
        df = pd.DataFrame([laptop_data])
        
        # Faire la prédiction
        predicted_price = model.predict(df)[0]
        
        # Formater le prix (déjà en dollars)
        formatted_price = round(predicted_price, 2)
        
        return jsonify({
            'success': True,
            'predicted_price': formatted_price,
            'message': f'Prix estimé: ${formatted_price:,.2f} USD'
        })
        
    except ValueError as e:
        return jsonify({
            'error': f'Erreur de validation: {str(e)}'
        }), 400
    except Exception as e:
        return jsonify({
            'error': f'Erreur lors de la prédiction: {str(e)}'
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """Endpoint de santé pour Render"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
