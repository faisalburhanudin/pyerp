from flask import Flask
from erp.view import admin, employee
from erp.model import db
from flask_login import LoginManager
from erp.model import Users
from erp.auth import bcrypt


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1/erp'


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return Users.query.filter_by(id=user_id).first()


app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(admin.bp)
app.register_blueprint(employee.bp)

db.init_app(app)
login_manager.init_app(app)
bcrypt.init_app(app)
