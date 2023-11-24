from flask import Flask
from app.routes.error_handler import ErrorHandler
from app.routes.api import ApiRouter
from app.routes.site import SiteRouter


class Router:
    def init_app(self, app: Flask) -> None:
        ErrorHandler(app)
        ApiRouter(app)
        SiteRouter(app)


router = Router()
