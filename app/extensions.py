from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

news_api = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=9af08da3227a4ce2826ddbc840650679"
