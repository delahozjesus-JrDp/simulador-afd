from afd.automata import AutomataFinitoDeterminista
from afd.validator import validar_afd


def crear_afd_par_ceros():
    return AutomataFinitoDeterminista(
        ["q0", "q1"], ["0", "1"],
        {("q0", "0"): "q1", ("q0", "1"): "q0",
         ("q1", "0"): "q0", ("q1", "1"): "q1"},
        "q0", ["q0"]
    )


def test_palabra_vacia():
    resultado = crear_afd_par_ceros().reconocer_palabra("")
    assert resultado["aceptada"] is True
    assert resultado["recorrido"] == ["q0"]


def test_palabra_aceptada():
    assert crear_afd_par_ceros().reconocer_palabra("1001")["aceptada"] is True


def test_palabra_rechazada():
    assert crear_afd_par_ceros().reconocer_palabra("10")["aceptada"] is False


def test_simbolo_invalido():
    resultado = crear_afd_par_ceros().reconocer_palabra("102")
    assert resultado["motivo"] == "simbolo_invalido"
    assert resultado["simbolo_invalido"] == "2"
    assert resultado["posicion"] == 3


def test_validacion_correcta():
    afd = crear_afd_par_ceros()
    resultado = validar_afd(afd.estados, afd.alfabeto, afd.transiciones,
                            afd.estado_inicial, afd.estados_finales)
    assert resultado["valido"] is True
