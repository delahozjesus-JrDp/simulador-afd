# Informe de desarrollo

## Objetivo
Implementar una aplicación web académica para construir y simular autómatas finitos deterministas.

## Tecnologías
Python, Flask, HTML, CSS, JavaScript y Pytest. No se utiliza base de datos.

## Componentes
1. Construcción y validación de la quíntupla.
2. Generación de hasta cinco palabras reconocidas más cortas, con longitud máxima 10.
3. Reconocimiento de palabras ingresadas y visualización de recorridos.

## Pruebas
Ejecutar `python -m pytest -v`. Los casos incluidos cubren palabra vacía, aceptación, rechazo, símbolo inválido, validación, generación de palabras y rutas principales.

## Limitaciones
El AFD activo se conserva en memoria del proceso Flask; al detener el servidor debe construirse nuevamente. El servidor incluido es de desarrollo y no está destinado a producción.
