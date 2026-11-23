# Simulador de Autómatas Finitos Deterministas (AFD)

Aplicación académica desarrollada con Python, Flask, HTML, CSS y JavaScript.

## 1. Requisitos previos

- Windows 10 o Windows 11.
- Python 3.10 o superior. El proyecto fue preparado y probado durante el desarrollo con Python 3.14.4.
- Conexión a Internet la primera vez que se instalen las dependencias.
- No es necesario instalar Flask ni pytest manualmente: el archivo `.bat` lo hace automáticamente.

### Verificar Python

Abre PowerShell o CMD y ejecuta:

```powershell
py --version
```

Si el comando `py` no está disponible, prueba:

```powershell
python --version
```

Si Python no está instalado, descárgalo desde https://www.python.org/downloads/.
Durante la instalación en Windows, activa la opción **Add Python to PATH**.

## 2. Instalación e inicio rápido en Windows

La forma más sencilla de instalar y ejecutar el proyecto es:

1. Descarga o clona el repositorio.
2. Descomprime el proyecto si lo descargaste como ZIP.
3. Abre la carpeta principal `simulador_afd`.
4. Haz doble clic en `INICIAR_SIMULADOR.bat`.
5. Espera a que el archivo prepare el entorno virtual e instale las dependencias.
6. Cuando aparezca el mensaje de inicio, abre el navegador en:

   http://127.0.0.1:5000

La primera ejecución requiere conexión a Internet para descargar Flask y pytest. Las siguientes ejecuciones reutilizan el entorno virtual `.venv` y verifican las dependencias instaladas.

Para detener el servidor, vuelve a la ventana del archivo `.bat` y presiona `CTRL + C`.

## 3. Instalación manual en Windows (PowerShell)

Si prefieres ejecutar cada paso manualmente, abre PowerShell en la carpeta raíz del proyecto y ejecuta:

### Paso 1. Crear el entorno virtual

```powershell
py -3 -m venv .venv
```

Si no tienes disponible el lanzador `py`, utiliza:

```powershell
python -m venv .venv
```

### Paso 2. Activar el entorno virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación, ejecuta primero:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Y vuelve a activar:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Paso 3. Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

### Paso 4. Ejecutar la aplicación

```powershell
python app.py
```

Abre http://127.0.0.1:5000 en el navegador.

## 4. Dependencias del proyecto

Las dependencias de Python se encuentran fijadas en `requirements.txt`:

| Dependencia | Versión | Uso |
|---|---:|---|
| Flask | 3.1.3 | Servidor web y rutas de la aplicación |
| pytest | 9.2.0 | Ejecución de pruebas automatizadas |

También se utiliza el módulo `venv` de Python para crear un entorno virtual aislado. `pip` instala las dependencias indicadas en `requirements.txt`.

No se requiere instalar una base de datos, Docker, Graphviz ni bibliotecas externas de autómatas. La representación gráfica del AFD se dibuja mediante JavaScript y SVG en el navegador.

## 5. Ejecutar las pruebas

Las pruebas permiten comprobar el comportamiento del autómata, los módulos y las rutas de la aplicación.

Con el entorno virtual activado, ejecuta:

```powershell
python -m pytest -v
```

También puedes ejecutarlas sin activar el entorno virtual:

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

## 6. Uso de la aplicación

1. Entra a **Construir AFD**.
2. Escribe los estados separados por comas, por ejemplo `q0, q1`.
3. Escribe los símbolos del alfabeto separados por comas, por ejemplo `0, 1`.
4. Selecciona el estado inicial y los estados finales.
5. Genera y completa todas las transiciones.
6. Construye el autómata.
7. Consulta la quíntupla, la tabla de transiciones y el diagrama.
8. Utiliza los módulos 2 y 3 para generar palabras reconocidas y probar palabras.

El AFD activo se conserva en memoria mientras el proceso Flask siga encendido. Si detienes el servidor, debes volver a construirlo.

## 7. Ejemplo: cantidad par de ceros

- Q: `q0, q1`
- Σ: `0, 1`
- Estado inicial: `q0`
- Estados finales: `q0`
- δ(q0,0)=q1
- δ(q0,1)=q0
- δ(q1,0)=q0
- δ(q1,1)=q1

Palabras esperadas en el módulo 2: ε, `1`, `00`, `11`, `001`.

## 8. Estructura del proyecto

- `afd/`: modelo, validación, generación de palabras y representación del autómata.
- `routes/`: rutas Flask.
- `templates/`: páginas HTML.
- `static/`: estilos y JavaScript.
- `tests/`: pruebas automatizadas.
- `docs/`: material de estudio y sustentación.
- `ejemplos/`: ejemplos de autómatas.
- `informes/`: informe de desarrollo.
- `INICIAR_SIMULADOR.bat`: prepara el entorno e inicia la aplicación.
- `requirements.txt`: dependencias de Python.

## 9. Solución de problemas frecuentes

**El comando `py` o `python` no se reconoce**

Instala Python 3.10 o superior y marca **Add Python to PATH** durante la instalación. Cierra y vuelve a abrir la terminal.

**No se pueden descargar las dependencias**

Verifica la conexión a Internet y vuelve a ejecutar `INICIAR_SIMULADOR.bat`. También puedes instalar manualmente con `python -m pip install -r requirements.txt`.

**La dirección `127.0.0.1:5000` no abre**

Verifica que la ventana del `.bat` siga abierta y que Flask no haya mostrado un error. Si el puerto 5000 está ocupado, cierra la otra aplicación que lo utiliza.

**PowerShell no permite activar `.venv`**

Ejecuta `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` en esa misma ventana y vuelve a activar el entorno. Este paso solo afecta la sesión actual de PowerShell.

## 10. Uso de herramientas de IA

Este proyecto recibió asistencia de IA para estructurar archivos, explicar conceptos, proponer código, preparar pruebas y apoyar la depuración. El equipo debe revisar, comprender, validar y adaptar cada componente, y declarar el uso de IA de acuerdo con las reglas de su curso. Cada integrante debe poder explicar y modificar el código que presenta.
