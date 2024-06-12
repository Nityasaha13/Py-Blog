from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.models.user import User
from app.extensions import db, news_api
from app.blueprints.posts import bp
import requests

auth = Blueprint('auth', __name__)


@bp.route("/")
def home():
    response = requests.get(news_api)
    news_data = response.json()
    articles = news_data.get('articles', [])
    return render_template('news-home-page.html',articles=articles)


@auth.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Logged in successfully!", "success")
            return redirect(url_for("post.index"))  # Change "index" to the name of your homepage route
        else:
            flash("Invalid email or password", "error")
    return render_template('auth/login.html')


@auth.route("/registration/", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email address already exists", "error")
        else:
            new_user = User(name=name, email=email, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully! You can now log in.", "success")
            return redirect(url_for("auth.login"))  
    return render_template('auth/registration.html')


@auth.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for("post.index"))
