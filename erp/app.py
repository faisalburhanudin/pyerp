from flask import Flask
from erp.view import admin
from erp.model import db


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1/erp'


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(admin.bp)
db.init_app(app)
