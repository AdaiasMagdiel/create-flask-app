from flask import Flask
import traceback


class ErrorHandler:
    def __init__(self, app: Flask) -> None:
        app.register_error_handler(400, self.error)
        app.register_error_handler(404, self.error)
        app.register_error_handler(422, self.error)

    def error(self, e):
        traceback.print_exc()
        code = e.code if hasattr(e, 'code') else 500

        return {'error': e.description, 'code': code}, code
