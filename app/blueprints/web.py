from flask import Blueprint, request, render_template

bp = Blueprint("web",__name__)

@bp.route("/")
def index():
    return render_template('blog/index.html')


@bp.route("/login/")
def login():
    return render_template('auth/login.html')


@bp.route("/registration/")
def registration():
    return render_template('auth/registration.html')