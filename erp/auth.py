from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from erp.model import Users

login_manager = LoginManager()
bcrypt = Bcrypt()


@login_manager.user_loader
def load_user(user_id):
    return Users.query.filter_by(id=user_id).first()
