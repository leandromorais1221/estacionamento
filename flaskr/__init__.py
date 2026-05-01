from flask import Flask
from flaskr.controllers.site_controller import site_bp
from flaskr.models import *

def create_app():
    app = Flask(__name__, template_folder="./views")
    app.secret_key = "b215e562c033ef21a689f7963ad99c97"
    app.register_blueprint(site_bp)

    db.connect()
    db.create_tables([Proprietario, Tipo, Cor, Veiculo, Movimentacao, TabelaPreco], safe=True)

    return app