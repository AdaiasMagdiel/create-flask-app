from flask import Flask


class ErrorHandler:
    def __init__(self, app: Flask) -> None:
        app.register_error_handler(400, self.error_400)
        app.register_error_handler(404, self.error_404)
        app.register_error_handler(422, self.error_422)

    def error_400(self, e):
        return {'error': e.description}, 400

    def error_404(self, e):
        return {'error': 'The current endpoint was not found'}, 404

    def error_422(self, e):
        return {'error': e.description}, 422
