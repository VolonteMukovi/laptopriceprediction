@echo off
echo ========================================
echo Installation de l'environnement Python 3.13
echo ========================================
echo.

echo Suppression de l'ancien environnement virtuel...
if exist venv rmdir /s /q venv

echo.
echo Creation du nouvel environnement virtuel avec Python 3.13...
py -3.13 -m venv venv

echo.
echo Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

echo.
echo Mise a jour de pip...
python -m pip install --upgrade pip

echo.
echo Installation des dependances...
pip install -r requirements.txt

echo.
echo ========================================
echo Installation terminee!
echo ========================================
echo.
echo Pour activer l'environnement virtuel plus tard:
echo   venv\Scripts\activate.bat
echo.
echo Pour lancer l'application:
echo   python app.py
echo.
pause

