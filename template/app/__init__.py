from flask import Flask
from app.settings import settings
from app.routes import router


def create_app() -> Flask:
    app = Flask(__name__)

    settings.init_app(app)
    router.init_app(app)

    return app
