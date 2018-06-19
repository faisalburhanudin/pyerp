from flask import Blueprint, render_template, request, redirect
from erp.model import Users

bp = Blueprint("admin", __name__, url_prefix='/admin')


@bp.route('/')
def admin():
    return redirect('/admin/employee')


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
