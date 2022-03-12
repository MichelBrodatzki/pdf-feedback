from flask import (
    Blueprint
)

bp = Blueprint('frontend', __name__, url_prefix='/')
@bp.route("/", methods=('GET',))
def index():
    return "Hello, World! (Frontend)"