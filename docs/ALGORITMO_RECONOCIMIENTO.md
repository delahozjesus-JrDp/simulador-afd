# Algoritmo de reconocimiento

1. Colocar el estado actual en q0.
2. Registrar q0 en el recorrido.
3. Leer cada símbolo de la palabra de izquierda a derecha.
4. Si el símbolo no pertenece a Σ, detener el procesamiento e informar el símbolo y su posición.
5. Si pertenece a Σ, consultar δ(estado actual, símbolo).
6. Actualizar el estado actual y agregarlo al recorrido.
7. Al terminar la palabra, aceptar si el estado actual pertenece a F; de lo contrario, rechazar.

Para ε no se ejecuta el ciclo: se evalúa directamente si q0 pertenece a F.
