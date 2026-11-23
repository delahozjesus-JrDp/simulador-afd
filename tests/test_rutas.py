from app import crear_aplicacion


def test_inicio_responde():
    app = crear_aplicacion()
    app.config["TESTING"] = True
    cliente = app.test_client()
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200


def test_modulos_piden_afd():
    app = crear_aplicacion()
    app.config["TESTING"] = True
    cliente = app.test_client()
    assert cliente.get("/modulo2").status_code == 302
    assert cliente.get("/modulo3").status_code == 302
