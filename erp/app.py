from flask import Flask
from erp.view import admin
from erp.model import db


app = Flask(__name__)

app.register_blueprint(admin.bp)

db.init_app(app)
