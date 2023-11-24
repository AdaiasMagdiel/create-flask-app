from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix="/api")


@bp.get('/')
def index():
    return {'olá': 'mundo'}
