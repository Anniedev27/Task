from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, Integer, String, Date

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

class Todo(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column(unique=True)
    date: Mapped[str]
    

with app.app_context():
    db.create_all()


    