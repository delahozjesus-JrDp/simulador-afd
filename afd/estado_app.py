# El AFD se conserva mientras el proceso Flask permanezca encendido.
afd_activo = None


def obtener_afd_activo():
    return afd_activo


def activar_afd(nuevo_afd):
    global afd_activo
    afd_activo = nuevo_afd


def limpiar_afd():
    global afd_activo
    afd_activo = None
