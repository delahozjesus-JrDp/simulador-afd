# Simulador de Autómatas Finitos Deterministas (AFD)

Aplicación académica desarrollada con Python, Flask, HTML, CSS y JavaScript.

## Requisitos
- Python 3.10 o superior
- Windows, macOS o Linux

## Instalación en Windows (PowerShell)
Abre una terminal en la carpeta del proyecto:

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Ejecutar
```powershell
python app.py
```
Abre http://127.0.0.1:5000

Para detener el servidor: `Ctrl + C`.

## Ejecutar pruebas
En otra terminal, activa el entorno virtual y ejecuta:

```powershell
python -m pytest -v
```

## Uso
1. Entra a **Construir AFD**.
2. Escribe estados separados por comas, por ejemplo `q0, q1`.
3. Escribe símbolos separados por comas, por ejemplo `0, 1`.
4. Selecciona el estado inicial y los estados finales.
5. Genera y completa todas las transiciones.
6. Construye el autómata.
7. Consulta la quíntupla, la tabla y el diagrama; después utiliza los módulos 2 y 3.

El AFD activo se conserva en memoria mientras el proceso Flask siga encendido. Si detienes el servidor, debes volver a construirlo.

## Ejemplo: cantidad par de ceros
- Q: `q0, q1`
- Σ: `0, 1`
- Estado inicial: `q0`
- Estados finales: `q0`
- δ(q0,0)=q1; δ(q0,1)=q0; δ(q1,0)=q0; δ(q1,1)=q1

Palabras esperadas en el módulo 2: ε, `1`, `00`, `11`, `001`.

## Estructura
- `afd/`: modelo, validación, generación de palabras y representación DOT.
- `routes/`: rutas Flask.
- `templates/`: páginas HTML.
- `static/`: estilos y JavaScript.
- `tests/`: pruebas automatizadas.
- `docs/`: material de estudio y sustentación.

## Uso de herramientas de IA
Este proyecto recibió asistencia de IA para estructurar archivos, explicar conceptos, proponer código, preparar pruebas y apoyar la depuración. El equipo debe revisar, comprender, validar y adaptar cada componente, y declarar el uso de IA de acuerdo con las reglas de su curso. Cada integrante debe poder explicar y modificar el código que presenta.
