from flask import Flask
from app.blueprints import web, posts
from app.extensions import db, login_manager
from app.models.user import User
from flask_login import LoginManager

app = Flask(__name__)

app.register_blueprint(web.auth)
app.register_blueprint(posts.bp)

app.config["DEBUG"]=True

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SECRET_KEY"] = "py-blog-flask" 
# initialize the app with the extension
db.init_app(app)


with app.app_context():
    db.create_all()


from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

