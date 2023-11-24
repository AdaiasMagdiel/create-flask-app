from flask import Blueprint

bp = Blueprint('site', __name__)


@bp.get('/')
def index():
    return 'Olá, Mundo!'
