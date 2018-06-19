from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Enum
from erp.auth import bcrypt

db = SQLAlchemy()


class Users(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)

    username = Column(String(45))

    password = Column(String(150))

    role = Column(String(45))

    email = Column(String(45))

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def validate_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


class RewardPunish(db.Model):
    id = Column(Integer, primary_key=True)

    name = Column(String(20), nullable=False)

    type = Column(Integer, nullable=False)
