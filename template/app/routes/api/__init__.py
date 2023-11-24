from flask import Blueprint, Flask
from app.routes.api import routes


class ApiRouter:
    def __init__(self, app: Flask) -> None:
        api = Blueprint("api", __name__)

        api.register_blueprint(routes.bp)

        app.register_blueprint(api)
