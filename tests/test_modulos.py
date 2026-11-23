from afd.automata import AutomataFinitoDeterminista
from afd.word_generator import obtener_cinco_palabras, obtener_estados_coalcanzables


def crear_afd(estados, alfabeto, transiciones, inicial, finales):
    return AutomataFinitoDeterminista(estados, alfabeto, transiciones, inicial, finales)


def test_cinco_palabras_par_ceros():
    afd = crear_afd(["q0","q1"], ["0","1"],
        {("q0","0"):"q1",("q0","1"):"q0",("q1","0"):"q0",("q1","1"):"q1"},
        "q0", ["q0"])
    assert [x["palabra"] for x in obtener_cinco_palabras(afd)] == ["", "1", "00", "11", "001"]


def test_cinco_palabras_termina_ab():
    afd = crear_afd(["s0","s1","s2"], ["a","b"],
        {("s0","a"):"s1",("s0","b"):"s0",("s1","a"):"s1",
         ("s1","b"):"s2",("s2","a"):"s1",("s2","b"):"s0"},
        "s0", ["s2"])
    assert [x["palabra"] for x in obtener_cinco_palabras(afd)] == ["ab","aab","bab","aaab","abab"]


def test_solo_reconoce_ab_ba():
    afd = crear_afd(["p0","p1","p2","p3","m"], ["a","b"],
        {("p0","a"):"p1",("p0","b"):"p2",("p1","a"):"m",("p1","b"):"p3",
         ("p2","a"):"p3",("p2","b"):"m",("p3","a"):"m",("p3","b"):"m",
         ("m","a"):"m",("m","b"):"m"}, "p0", ["p3"])
    assert [x["palabra"] for x in obtener_cinco_palabras(afd)] == ["ab","ba"]


def test_afd_sin_palabras():
    afd = crear_afd(["q0","q1"], ["a"],
        {("q0","a"):"q0",("q1","a"):"q1"}, "q0", ["q1"])
    assert obtener_cinco_palabras(afd) == []


def test_limite_longitud():
    afd = crear_afd(["s0","s1","s2"], ["a","b"],
        {("s0","a"):"s1",("s0","b"):"s0",("s1","a"):"s1",
         ("s1","b"):"s2",("s2","a"):"s1",("s2","b"):"s0"},
        "s0", ["s2"])
    assert [x["palabra"] for x in obtener_cinco_palabras(afd, limite_longitud=2)] == ["ab"]


def test_estados_coalcanzables():
    afd = crear_afd(["p0","p1","p2","p3","m"], ["a","b"],
        {("p0","a"):"p1",("p0","b"):"p2",("p1","a"):"m",("p1","b"):"p3",
         ("p2","a"):"p3",("p2","b"):"m",("p3","a"):"m",("p3","b"):"m",
         ("m","a"):"m",("m","b"):"m"}, "p0", ["p3"])
    assert obtener_estados_coalcanzables(afd) == {"p0","p1","p2","p3"}
