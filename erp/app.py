import os

from flask import Flask
from erp.view import admin, employee, reward_punish, home, application, presence
from erp.model import db
from flask_login import LoginManager
from erp.model import Users
from erp.auth import bcrypt

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1/erp'
    # SQLALCHEMY_ECHO = True

    UPLOAD_FOLDER = os.path.join(CURRENT_DIR, 'uploads')


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return Users.query.filter_by(id=user_id).first()


app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(home.bp)
app.register_blueprint(admin.bp)
app.register_blueprint(employee.bp)
app.register_blueprint(reward_punish.bp)
app.register_blueprint(application.bp)
app.register_blueprint(presence.bp)

db.init_app(app)
login_manager.init_app(app)
bcrypt.init_app(app)
