from sqlalchemy.orm import Mapped, mapped_column
from app.extensions import db
from flask_login import UserMixin

# Create user model
class Users(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)