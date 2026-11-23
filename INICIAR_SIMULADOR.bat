@echo off
setlocal
chcp 65001 >nul
title Simulador de Automatas Finitos Deterministas

REM Trabajar siempre desde la carpeta donde esta este archivo.
cd /d "%~dp0"

echo.
echo ================================================
echo       SIMULADOR DE AUTOMATAS FINITOS (AFD)
echo ================================================
echo.

REM Detectar Python. Se prefiere el lanzador py de Windows.
where py >nul 2>nul
if %errorlevel%==0 (
    set "PYTHON_CMD=py -3"
) else (
    where python >nul 2>nul
    if %errorlevel%==0 (
        set "PYTHON_CMD=python"
    ) else (
        echo ERROR: No se encontro Python instalado.
        echo Instala Python 3.10 o superior desde https://www.python.org/downloads/
        echo Durante la instalacion marca la opcion "Add Python to PATH".
        echo Despues vuelve a ejecutar este archivo.
        pause
        exit /b 1
    )
)

echo [1/3] Comprobando Python...
call %PYTHON_CMD% --version
if errorlevel 1 (
    echo ERROR: No fue posible ejecutar Python.
    pause
    exit /b 1
)

echo.
echo [2/3] Preparando el entorno virtual...
if not exist ".venv\Scripts\python.exe" (
    call %PYTHON_CMD% -m venv .venv
    if errorlevel 1 (
        echo ERROR: No se pudo crear el entorno virtual.
        pause
        exit /b 1
    )
)

echo.
echo Instalando o verificando las dependencias...
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: No se pudieron instalar las dependencias.
    echo Verifica tu conexion a Internet e intenta nuevamente.
    pause
    exit /b 1
)

echo.
echo [3/3] Iniciando el simulador...
echo.
echo Abre tu navegador en: http://127.0.0.1:5000
echo Para detener el servidor, presiona CTRL + C en esta ventana.
echo.

".venv\Scripts\python.exe" app.py

echo.
echo El servidor del simulador se ha detenido.
pause
endlocal
