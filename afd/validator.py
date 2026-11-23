def validar_afd(estados, alfabeto, transiciones,
                estado_inicial, estados_finales):
    errores = []

    if not estados:
        errores.append("Debe existir al menos un estado.")
    if len(estados) != len(set(estados)):
        errores.append("Existen estados duplicados.")
    if any(not isinstance(e, str) or not e for e in estados):
        errores.append("Los estados no pueden estar vacíos.")

    if not alfabeto:
        errores.append("El alfabeto no puede estar vacío.")
    if len(alfabeto) != len(set(alfabeto)):
        errores.append("Existen símbolos duplicados.")
    for simbolo in alfabeto:
        if not isinstance(simbolo, str) or len(simbolo) != 1:
            errores.append(f"El símbolo '{simbolo}' debe tener exactamente un carácter.")

    if estado_inicial not in estados:
        errores.append("El estado inicial no pertenece a Q.")

    for estado in estados_finales:
        if estado not in estados:
            errores.append(f"El estado final '{estado}' no pertenece a Q.")

    esperadas = {(estado, simbolo) for estado in estados for simbolo in alfabeto}
    recibidas = set(transiciones)

    for estado, simbolo in sorted(esperadas - recibidas):
        errores.append(f"Falta la transición desde {estado} con el símbolo {simbolo}.")

    for clave, destino in transiciones.items():
        if not isinstance(clave, tuple) or len(clave) != 2:
            errores.append(f"La clave de transición '{clave}' no es válida.")
            continue
        estado, simbolo = clave
        if estado not in estados or simbolo not in alfabeto:
            errores.append(f"La transición '{clave}' utiliza un estado o símbolo no permitido.")
        if destino not in estados:
            errores.append(f"El destino '{destino}' no pertenece a Q.")

    return {"valido": not errores, "errores": errores}
