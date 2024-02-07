from flask import Flask
from app.settings import settings
from app.routes import Router


def create_app() -> Flask:
    app = Flask(__name__)

    settings.init_app(app)
    Router.init_app(app)

    return app
