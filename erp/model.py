import os
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from erp.auth import bcrypt

db = SQLAlchemy()


class Users(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)

    username = Column(String(45))

    password = Column(String(150))

    role = Column(String(45))

    email = Column(String(45))

    def total_reward(self):
        return UserRewardPunish.query.join(RewardPunish).filter(
            UserRewardPunish.user_id == self.id,
            RewardPunish.type == 1
        ).count()

    def total_punish(self):
        return UserRewardPunish.query.join(RewardPunish).filter(
            UserRewardPunish.user_id == self.id,
            RewardPunish.type == 2
        ).count()

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def validate_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


class RewardPunish(db.Model):
    id = Column(Integer, primary_key=True)

    name = Column(String(20), nullable=False)

    type = Column(Integer, nullable=False)


class Application(db.Model):
    id = Column(Integer, primary_key=True)

    name = Column(String(45), nullable=False)

    photo = Column(String(45), nullable=False)

    email = Column(String(45), nullable=False)

    birthday = Column(Date, nullable=False)

    resume = Column(String(45), nullable=False)

    year_experience = Column(Integer, nullable=False)

    def set_photo(self, file):
        filename = file.filename
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        self.photo = filename

    def set_resume(self, file):
        filename = file.filename
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        self.resume = filename


class UserRewardPunish(db.Model):
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    reward_punish_id = Column(Integer, ForeignKey('reward_punish.id'), nullable=False)


class Absence(db.Model):
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    date_time = Column(DateTime, nullable=False)
