from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()


class User(db.Model):
    id = Column(Integer, primary_key=True)

    username = Column(String(45))

    password = Column(String(150))

    role = Column(String(45))

    email = Column(String(45))
