from flask import Flask
from app.blueprints import web, posts
from app.extensions import db

app = Flask(__name__)

app.register_blueprint(web.bp)
app.register_blueprint(posts.bp)


# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


with app.app_context():
    db.create_all()
