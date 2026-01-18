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
MODEL_PATH = 'laptop_price_model.pkl'
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
            raise
        except Exception as e:
            print(f"❌ Erreur lors du chargement du modèle: {str(e)}")
            raise
    return model

# Charger le modèle au démarrage
load_model()

@app.route('/')
def index():
    """Page d'accueil"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint pour la prédiction du prix"""
    try:
        # Récupérer les données du formulaire
        data = request.get_json()
        
        # Vérifier que tous les champs requis sont remplis
        required_fields = ['brand', 'processor', 'CPU', 'Ram', 'Ram_type', 
                          'ROM', 'ROM_type', 'GPU', 'OS']
        for field in required_fields:
            if not data.get(field, '').strip():
                return jsonify({
                    'error': f'Le champ {field} est requis'
                }), 400
        
        # Vérifier les champs numériques
        numeric_fields = ['spec_rating', 'display_size', 'resolution_width', 'resolution_height']
        for field in numeric_fields:
            value = data.get(field)
            if value is None or value == '':
                return jsonify({
                    'error': f'Le champ {field} est requis et doit être un nombre'
                }), 400
            try:
                float(value)
            except (ValueError, TypeError):
                return jsonify({
                    'error': f'Le champ {field} doit être un nombre valide'
                }), 400
        
        # Créer un dictionnaire avec les données
        laptop_data = {
            'brand': data.get('brand', '').lower().strip(),
            'processor': data.get('processor', '').strip(),
            'CPU': data.get('CPU', '').strip(),
            'Ram': data.get('Ram', '').strip(),
            'Ram_type': data.get('Ram_type', '').strip(),
            'ROM': data.get('ROM', '').strip(),
            'ROM_type': data.get('ROM_type', '').strip(),
            'GPU': data.get('GPU', '').strip(),
            'OS': data.get('OS', '').strip(),
            'spec_rating': float(data.get('spec_rating')),
            'display_size': float(data.get('display_size')),
            'resolution_width': float(data.get('resolution_width')),
            'resolution_height': float(data.get('resolution_height'))
        }
        
        # Convertir en DataFrame
        df = pd.DataFrame([laptop_data])
        
        # Faire la prédiction
        predicted_price = model.predict(df)[0]
        
        # Formater le prix
        formatted_price = round(predicted_price, 2)
        
        return jsonify({
            'success': True,
            'predicted_price': formatted_price,
            'message': f'Prix estimé: ₹{formatted_price:,.2f}'
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

