from flask import Blueprint,render_template

bp = Blueprint("dilipala",__name__,url_prefix="/dilipala")

@bp.route("/")
def index():
    return render_template("dilipala.html")