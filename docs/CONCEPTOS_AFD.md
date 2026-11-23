# Conceptos fundamentales del AFD

Un autómata finito determinista se define como M = (Q, Σ, δ, q0, F):

- Q: conjunto finito y no vacío de estados.
- Σ: alfabeto finito de símbolos.
- δ: función de transición Q × Σ → Q.
- q0: estado inicial perteneciente a Q.
- F: conjunto de estados finales, subconjunto de Q.

Es determinista porque para cada par (estado, símbolo) existe exactamente un destino. Es completo cuando existe una transición para todos los elementos de Q × Σ.

Una palabra es aceptada si, después de leer todos sus símbolos desde q0, el autómata termina en un estado de F. La palabra vacía ε no consume símbolos: su estado final es q0.
