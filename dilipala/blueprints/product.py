from flask import Blueprint

bp = Blueprint("product",__name__,url_prefix="/")

@bp.route("/")
def index():
    return "hello"