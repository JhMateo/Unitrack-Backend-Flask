import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    enviroment_configuration = os.getenv("CONFIGURATION_SETUP")

    app.config.from_object(enviroment_configuration)

    db.init_app(app)

    with app.app_context():
        # Definir la API con blueprints
        from aplication.stop_api import stop_api_blueprint
        app.register_blueprint(stop_api_blueprint)
        return app