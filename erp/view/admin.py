from flask import Blueprint, render_template, request, redirect
from erp.model import Users

bp = Blueprint("admin", __name__, url_prefix='/admin')


@bp.route('/')
def admin():
    return render_template('admin/home.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = Users.query.filter_by(
            email=email
        ).first()

        is_valid = user.validate_password(password)
        if is_valid:
            url_next = request.args.get('next')
            return redirect(url_next or '/admin')

    return render_template('admin/login.html')


@bp.route('/presence')
def presence():
    return render_template('admin/presence.html')


@bp.route('/reward-and-punishment')
def reward_and_punishment():
    return render_template('admin/reward-and-punish/list.html')


@bp.route('/add-reward')
def add_reward():
    return render_template('admin/reward-and-punish/add-reward.html')


@bp.route('/add-punish')
def add_punish():
    return render_template('admin/reward-and-punish/add-punish.html')


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
