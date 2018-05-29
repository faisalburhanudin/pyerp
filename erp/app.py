from flask import Flask
from erp.view import admin
from erp.model import db
from erp.auth import login_manager, bcrypt


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1/erp'


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(admin.bp)

db.init_app(app)
login_manager.init_app(app)
bcrypt.init_app(app)
