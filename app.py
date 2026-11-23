from flask import Flask
from routes.main import main

def crear_aplicacion():
    aplicacion = Flask(__name__)
    aplicacion.config["SECRET_KEY"] = "cambiar-esta-clave-en-produccion"
    aplicacion.register_blueprint(main)
    return aplicacion

app = crear_aplicacion()

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
