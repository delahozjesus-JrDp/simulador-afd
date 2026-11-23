from flask import Blueprint, render_template, request, redirect, url_for, flash, session

from afd.automata import AutomataFinitoDeterminista
from afd.validator import validar_afd
from afd.word_generator import obtener_cinco_palabras
from afd.estado_app import obtener_afd_activo, activar_afd, limpiar_afd
from afd.graph_dot import generar_grafico_dot, obtener_datos_grafo

main = Blueprint("main", __name__)


def dividir_lista(texto):
    return [parte.strip() for parte in texto.split(",") if parte.strip()]


@main.route("/")
def inicio():
    return render_template("index.html", afd=obtener_afd_activo())


@main.route("/construir", methods=["GET", "POST"])
def construir():
    if request.method == "POST":
        estados = dividir_lista(request.form.get("estados", ""))
        alfabeto = dividir_lista(request.form.get("alfabeto", ""))
        estado_inicial = request.form.get("estado_inicial", "").strip()
        estados_finales = request.form.getlist("estados_finales")

        transiciones = {}
        for i, estado in enumerate(estados):
            for j, simbolo in enumerate(alfabeto):
                destino = request.form.get(f"transicion_{i}_{j}", "").strip()
                if destino:
                    transiciones[(estado, simbolo)] = destino

        validacion = validar_afd(
            estados, alfabeto, transiciones, estado_inicial, estados_finales
        )
        if not validacion["valido"]:
            for error in validacion["errores"]:
                flash(error, "error")
            return redirect(url_for("main.construir"))

        nuevo_afd = AutomataFinitoDeterminista(
            estados, alfabeto, transiciones, estado_inicial, estados_finales
        )
        activar_afd(nuevo_afd)
        session["historial_palabras"] = []
        flash("Autómata construido correctamente.", "success")
        if not estados_finales:
            flash("F está vacío: el autómata no aceptará ninguna palabra.", "warning")
        return redirect(url_for("main.automata"))

    return render_template("construir.html")


@main.route("/automata")
def automata():
    afd = obtener_afd_activo()
    if afd is None:
        flash("Primero debes construir un autómata.", "warning")
        return redirect(url_for("main.construir"))
    return render_template(
        "automata.html",
        afd=afd,
        grafico_dot=generar_grafico_dot(afd),
        datos_grafo=obtener_datos_grafo(afd),
    )


@main.route("/modulo2")
def modulo2():
    afd = obtener_afd_activo()
    if afd is None:
        flash("Primero debes construir un autómata.", "warning")
        return redirect(url_for("main.construir"))
    palabras = obtener_cinco_palabras(afd, limite_longitud=10, cantidad=5)
    return render_template("modulo2.html", palabras=palabras)


@main.route("/modulo3", methods=["GET", "POST"])
def modulo3():
    afd = obtener_afd_activo()
    if afd is None:
        flash("Primero debes construir un autómata.", "warning")
        return redirect(url_for("main.construir"))

    resultado = None
    palabra = None
    historial = session.get("historial_palabras", [])

    if request.method == "POST":
        palabra = request.form.get("palabra", "")
        resultado = afd.reconocer_palabra(palabra)
        registro = {
            "palabra": palabra,
            "aceptada": resultado["aceptada"],
            "motivo": resultado["motivo"],
            "recorrido": resultado["recorrido"],
            "estado_final": resultado["estado_final"],
            "simbolo_invalido": resultado["simbolo_invalido"],
            "posicion": resultado["posicion"],
        }
        historial.insert(0, registro)
        session["historial_palabras"] = historial[:20]

    return render_template(
        "modulo3.html",
        resultado=resultado,
        palabra=palabra,
        historial=session.get("historial_palabras", []),
    )


@main.route("/limpiar", methods=["POST"])
def limpiar():
    limpiar_afd()
    session.clear()
    flash("El autómata activo fue eliminado.", "success")
    return redirect(url_for("main.inicio"))


@main.route("/limpiar-historial", methods=["POST"])
def limpiar_historial():
    session.pop("historial_palabras", None)
    flash("Historial de pruebas eliminado.", "success")
    return redirect(url_for("main.modulo3"))
