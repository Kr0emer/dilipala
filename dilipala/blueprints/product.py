from flask import Blueprint,render_template
from models import ProductModel
bp = Blueprint("product",__name__,url_prefix="/")

@bp.route("/")
def index():
    products = ProductModel.query.all()
    return render_template("index.html",products=products)