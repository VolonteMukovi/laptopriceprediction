# Guide d'Installation - Problème de Compatibilité Python

## ⚠️ Problème Identifié

Votre modèle `laptop_price_model.pkl` a été entraîné avec:
- **scikit-learn 1.7.2**
- **numpy 2.x** (avec `numpy._core`)

Ces versions **nécessitent Python 3.9 ou supérieur**.

Vous utilisez actuellement **Python 3.8**, qui ne peut pas installer numpy 2.x.

## ✅ Solution Recommandée: Mettre à jour Python

### Sur Windows:

1. **Téléchargez Python 3.9+ (ou 3.11 recommandé)**
   - Allez sur: https://www.python.org/downloads/
   - Téléchargez la dernière version (3.11 ou 3.12)

2. **Installez Python 3.9+**
   - ✅ Cochez "Add Python to PATH" lors de l'installation
   - ✅ Choisissez "Install for all users" si vous avez les droits admin

3. **Vérifiez l'installation**
   ```powershell
   python --version
   # Devrait afficher Python 3.9.x, 3.10.x, 3.11.x ou 3.12.x
   ```

4. **Recréez votre environnement virtuel**
   ```powershell
   # Désactiver l'ancien venv
   deactivate
   
   # Supprimer l'ancien venv
   Remove-Item -Recurse -Force venv
   
   # Créer un nouveau venv avec la nouvelle version de Python
   python -m venv venv
   
   # Activer le nouveau venv
   .\venv\Scripts\Activate.ps1
   
   # Si vous avez une erreur d'exécution de scripts:
   # Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

5. **Installez les dépendances**
   ```powershell
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. **Lancez l'application**
   ```powershell
   python app.py
   ```

## 🔄 Solution Alternative: Réentraîner le Modèle (Non Recommandé)

Si vous ne pouvez pas mettre à jour Python, vous devrez réentraîner le modèle avec des versions compatibles Python 3.8:

1. **Installez les versions compatibles**
   ```powershell
   pip install pandas==2.0.3 numpy==1.24.4 scikit-learn==1.3.2 joblib==1.3.2
   ```

2. **Réentraînez le modèle** (utilisez votre notebook `Untitled.ipynb`)

3. **Sauvegardez le nouveau modèle**
   ```python
   joblib.dump(model, "laptop_price_model.pkl")
   ```

⚠️ **Attention**: Cela peut affecter les performances du modèle.

## 📋 Versions Requises

### Pour Python 3.9+ (Recommandé):
```
Flask>=2.3.0
pandas>=2.0.0,<2.0.4
numpy>=2.0.0,<3.0.0
scikit-learn>=1.7.0,<2.0.0
joblib>=1.3.0
gunicorn>=20.1.0
```

### Pour Python 3.8 (Alternative):
```
Flask>=2.3.0
pandas>=2.0.0,<2.0.4
numpy>=1.24.0,<2.0.0
scikit-learn>=1.3.0,<1.4.0
joblib>=1.3.0
gunicorn>=20.1.0
```

## 🔍 Vérification

Après installation, vérifiez:
```python
import sys
import numpy
import sklearn

print(f"Python: {sys.version}")
print(f"NumPy: {numpy.__version__}")
print(f"Scikit-learn: {sklearn.__version__}")
```

Vous devriez voir:
- Python: 3.9.x ou supérieur
- NumPy: 2.0.x ou supérieur
- Scikit-learn: 1.7.x ou supérieur

