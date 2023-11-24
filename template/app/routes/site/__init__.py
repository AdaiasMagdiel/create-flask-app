from flask import Blueprint, Flask
from app.routes.site import routes


class SiteRouter:
    def __init__(self, app: Flask) -> None:
        site = Blueprint("site", __name__)

        site.register_blueprint(routes.bp)

        app.register_blueprint(site)
