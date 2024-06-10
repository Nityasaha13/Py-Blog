from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.extensions import db


class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    category: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)