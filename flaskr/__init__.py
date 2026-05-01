from flask import Flask
from flaskr.controllers.site_controller import site_bp

def create_app():
    app = Flask(__name__, template_folder="./views")
    app.secret_key = "b215e562c033ef21a689f7963ad99c97"
    app.register_blueprint(site_bp)

    return app