
@echo off
echo ======================================
echo   CORRIGIENDO ENTORNO DEL PROYECTO
echo ======================================

if not exist .venv\Scripts\python.exe (
    echo Creando entorno virtual...
    python -m venv .venv
)

echo.
echo Activando entorno virtual...
call .venv\Scripts\activate.bat

echo.
echo Actualizando pip...
python -m pip install --upgrade pip

echo.
echo Instalando Flask y Pytest...
python -m pip install Flask pytest

echo.
echo Verificando instalaciones...
python -c "import flask, pytest; print('INSTALACION CORRECTA')"

echo.
echo Version de Flask:
python -m pip show Flask

echo.
echo Version de Pytest:
python -m pytest --version

echo.
echo ======================================
echo   PROCESO FINALIZADO
echo ======================================
pause
