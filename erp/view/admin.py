from flask import Blueprint, render_template, request
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


@bp.route('/employee/new')
def employee_add():
    return render_template('admin/employee/new.html')


@bp.route('/employee/edit')
def employee_edit():
    user_id = request.args.get('id')
    user = Users.query.filter_by(
        id=user_id
    ).first()
    return render_template('admin/employee/edit.html', user=user)
