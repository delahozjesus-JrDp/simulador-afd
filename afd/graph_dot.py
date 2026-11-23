def generar_grafico_dot(afd):
    """Genera texto DOT, agrupando símbolos con igual origen y destino."""
    lineas = [
        "digraph AFD {",
        "  rankdir=LR;",
        '  graph [bgcolor="white"];',
        '  node [shape=circle, style="filled", fillcolor="#EAF2F8"];',
        '  edge [color="#34495E"];',
        '  inicio [shape=point, label=""];',
    ]

    for estado in afd.estados:
        forma = "doublecircle" if estado in afd.estados_finales else "circle"
        seguro = str(estado).replace('"', r'\"')
        lineas.append(f'  "{seguro}" [shape={forma}];')

    inicial = str(afd.estado_inicial).replace('"', r'\"')
    lineas.append(f'  inicio -> "{inicial}";')

    grupos = {}
    for (origen, simbolo), destino in afd.transiciones.items():
        grupos.setdefault((origen, destino), []).append(simbolo)

    for (origen, destino), simbolos in grupos.items():
        origen = str(origen).replace('"', r'\"')
        destino = str(destino).replace('"', r'\"')
        etiqueta = ", ".join(simbolos).replace('"', r'\"')
        lineas.append(f'  "{origen}" -> "{destino}" [label="{etiqueta}"];')

    lineas.append("}")
    return "\n".join(lineas)


def obtener_datos_grafo(afd):
    return {
        "estados": afd.estados,
        "alfabeto": afd.alfabeto,
        "inicial": afd.estado_inicial,
        "finales": [e for e in afd.estados if e in afd.estados_finales],
        "transiciones": [
            {"origen": origen, "simbolo": simbolo, "destino": destino}
            for (origen, simbolo), destino in afd.transiciones.items()
        ],
    }
