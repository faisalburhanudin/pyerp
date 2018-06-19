from flask import Blueprint, render_template, request, redirect

from erp.model import db, Users

bp = Blueprint("employee", __name__, url_prefix='/admin/employee')


@bp.route('/')
def employee():
    users = Users.query.all()
    return render_template(
        'admin/employee/list.html',
        users=users
    )


@bp.route('/new', methods=['GET', 'POST'])
def employee_add():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role")

        user = Users()
        user.username = username
        user.email = email
        user.role = role
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return redirect('/admin/employee')

    return render_template('admin/employee/new.html')


@bp.route('/edit', methods=["GET", "POST"])
def employee_edit():
    if request.method == "POST":
        user_id = request.form.get('id')
        user = Users.query.filter_by(id=user_id).first()

        username = request.form.get("username")
        email = request.form.get("email")
        role = request.form.get("role")

        user.username = username
        user.email = email
        user.role = role

        db.session.add(user)
        db.session.commit()

        return redirect('/admin/employee')

    user_id = request.args.get('id')
    user = Users.query.filter_by(
        id=user_id
    ).first()

    return render_template('admin/employee/edit.html', user=user)
