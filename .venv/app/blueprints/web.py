from flask import Blueprint, request, render_template

bp = Blueprint("web",__name__)

@bp.route("/")
def index():
    return render_template('home-page.html')
