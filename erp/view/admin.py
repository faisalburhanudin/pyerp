from flask import Blueprint, render_template
from erp.model import Users

bp = Blueprint("admin", __name__, url_prefix='/admin')


@bp.route('/')
def admin():
    return render_template('admin/home.html')


@bp.route('/presence')
def presence():
    return render_template('admin/presence.html')


@bp.route('/employee')
def employee():
    users = Users.query.all()
    return render_template(
        'admin/employee/list.html',
        users=users
    )
