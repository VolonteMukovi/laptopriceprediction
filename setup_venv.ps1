# Script PowerShell pour créer l'environnement virtuel avec Python 3.13

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Installation de l'environnement Python 3.13" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Supprimer l'ancien environnement virtuel
if (Test-Path "venv") {
    Write-Host "Suppression de l'ancien environnement virtuel..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force venv
}

# Créer le nouvel environnement virtuel avec Python 3.13
Write-Host "Création du nouvel environnement virtuel avec Python 3.13..." -ForegroundColor Green
py -3.13 -m venv venv

# Activer l'environnement virtuel
Write-Host "Activation de l'environnement virtuel..." -ForegroundColor Green
& .\venv\Scripts\Activate.ps1

# Mettre à jour pip
Write-Host "Mise à jour de pip..." -ForegroundColor Green
python -m pip install --upgrade pip

# Installer les dépendances
Write-Host "Installation des dépendances..." -ForegroundColor Green
pip install -r requirements.txt

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Installation terminée!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Pour lancer l'application:" -ForegroundColor Yellow
Write-Host "  python app.py" -ForegroundColor White
Write-Host ""

