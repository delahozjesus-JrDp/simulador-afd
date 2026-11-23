# Cómo funciona el código

## Modelo
`afd/automata.py` almacena Q, Σ, δ, q0 y F. El método `reconocer_palabra` recorre la palabra símbolo a símbolo y guarda el estado inicial y cada destino alcanzado.

## Validación
`afd/validator.py` comprueba que haya estados, que no existan duplicados, que los símbolos tengan un carácter, que q0 y F pertenezcan a Q y que cada combinación Q × Σ tenga una transición válida.

## Búsqueda de palabras
`afd/word_generator.py` utiliza una cola (BFS). La cola procesa primero las palabras más cortas. Dentro de cada nivel, agrega símbolos en el orden en que aparecen en el alfabeto. Antes calcula estados co-alcanzables recorriendo las transiciones inversas desde F, para descartar estados desde los que no se puede llegar a aceptación.

## Interfaz
Flask recibe el formulario, valida los datos y crea el objeto AFD. El estado activo se guarda en `afd/estado_app.py` durante la ejecución del servidor.
