from collections import deque


def obtener_estados_coalcanzables(afd):
    """Devuelve los estados desde los que se puede alcanzar algún estado final."""
    inversas = {estado: [] for estado in afd.estados}
    for (origen, _simbolo), destino in afd.transiciones.items():
        inversas[destino].append(origen)

    alcanzables = set(afd.estados_finales)
    pendientes = deque(afd.estados_finales)

    while pendientes:
        actual = pendientes.popleft()
        for anterior in inversas[actual]:
            if anterior not in alcanzables:
                alcanzables.add(anterior)
                pendientes.append(anterior)
    return alcanzables


def obtener_cinco_palabras(afd, limite_longitud=10, cantidad=5):
    """Busca palabras aceptadas por BFS, ordenadas por longitud y alfabeto."""
    if limite_longitud < 0 or cantidad <= 0:
        return []

    utiles = obtener_estados_coalcanzables(afd)
    if afd.estado_inicial not in utiles:
        return []

    resultados = []
    pendientes = deque([("", afd.estado_inicial)])

    while pendientes and len(resultados) < cantidad:
        palabra, estado = pendientes.popleft()

        if estado in afd.estados_finales:
            detalle = afd.reconocer_palabra(palabra)
            resultados.append({
                "palabra": palabra,
                "recorrido": detalle["recorrido"],
                "estado_final": detalle["estado_final"],
            })
            if len(resultados) == cantidad:
                break

        if len(palabra) >= limite_longitud:
            continue

        for simbolo in afd.alfabeto:
            destino = afd.obtener_estado_siguiente(estado, simbolo)
            if destino in utiles:
                pendientes.append((palabra + simbolo, destino))

    return resultados
