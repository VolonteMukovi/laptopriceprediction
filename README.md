# Prédiction de Prix d'Ordinateur Portable

Application Flask pour prédire le prix d'un ordinateur portable en fonction de ses caractéristiques techniques.

## 🚀 Fonctionnalités

- Interface intuitive avec Tailwind CSS
- Formulaire complet pour saisir les caractéristiques de l'ordinateur
- Prédiction de prix en temps réel
- Design moderne et responsive

## 📋 Prérequis

- **Python 3.9 ou supérieur** (nécessaire pour numpy 2.x)
- pip (gestionnaire de paquets Python)

> ⚠️ **Important**: Ce modèle nécessite numpy 2.x qui requiert Python 3.9+. Si vous utilisez Python 3.8, vous devez mettre à jour Python.

## 🔧 Installation Locale

1. Clonez le repository ou téléchargez les fichiers

2. Créez un environnement virtuel (recommandé):
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installez les dépendances:
```bash
pip install -r requirements.txt
```

4. Assurez-vous que le fichier `laptop_price_model.pkl` est présent dans le dossier racine

5. Lancez l'application:
```bash
python app.py
```

6. Ouvrez votre navigateur et allez à: `http://localhost:5000`

## 🌐 Déploiement sur Render

1. **Créer un compte Render**: Allez sur [render.com](https://render.com) et créez un compte

2. **Créer un nouveau Web Service**:
   - Cliquez sur "New +" puis "Web Service"
   - Connectez votre repository GitHub (ou utilisez Git)
   - Ou utilisez "Manual Deploy"

3. **Configuration du service**:
   - **Name**: laptop-price-prediction (ou votre choix)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

4. **Variables d'environnement** (optionnel):
   - PORT est géré automatiquement par Render

5. **Assurez-vous que les fichiers suivants sont présents**:
   - `app.py`
   - `requirements.txt`
   - `laptop_price_model.pkl`
   - `templates/index.html`
   - `.gitignore`

6. **Déployez**:
   - Render détectera automatiquement les changements
   - Le déploiement peut prendre quelques minutes
   - Votre application sera disponible à `https://votre-app.onrender.com`

## 📁 Structure du Projet

```
laptopprediction/
├── app.py                      # Application Flask principale
├── laptop_price_model.pkl      # Modèle de machine learning
├── data.csv                    # Données d'entraînement (optionnel)
├── requirements.txt            # Dépendances Python
├── README.md                   # Ce fichier
├── .gitignore                  # Fichiers à ignorer par Git
└── templates/
    └── index.html             # Interface utilisateur
```

## 🎯 Utilisation

1. Remplissez le formulaire avec les caractéristiques de l'ordinateur:
   - Marque
   - Système d'exploitation
   - Processeur et CPU
   - Mémoire RAM et stockage
   - Carte graphique
   - Taille et résolution d'écran
   - Note de spécification

2. Cliquez sur "Prédire le Prix"

3. Le prix estimé s'affichera en dessous du formulaire

## 📊 Caractéristiques du Modèle

Le modèle utilise:
- **Algorithme**: Random Forest Regressor
- **Préprocessing**: StandardScaler pour les variables numériques, OneHotEncoder pour les variables catégorielles
- **Métriques**: 
  - R² Score: ~0.80
  - MAE: ~13863

## 🔍 Caractéristiques Prises en Compte

- **Catégorielles**:
  - Marque (brand)
  - Processeur (processor)
  - CPU (CPU)
  - RAM (Ram)
  - Type de RAM (Ram_type)
  - Stockage (ROM)
  - Type de stockage (ROM_type)
  - Carte graphique (GPU)
  - Système d'exploitation (OS)

- **Numériques**:
  - Note de spécification (spec_rating)
  - Taille d'écran (display_size)
  - Largeur de résolution (resolution_width)
  - Hauteur de résolution (resolution_height)

## ⚠️ Notes Importantes

- Le modèle a été entraîné sur des données spécifiques et les prédictions sont des estimations
- Les prix sont en Roupies indiennes (₹)
- Le modèle gère les valeurs inconnues grâce à `handle_unknown='ignore'` dans OneHotEncoder

## 📝 Licence

Ce projet est fourni tel quel pour usage éducatif et personnel.

## 🛠️ Support

Pour toute question ou problème, veuillez créer une issue dans le repository.

