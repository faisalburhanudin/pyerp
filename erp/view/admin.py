from flask import Blueprint, render_template

bp = Blueprint("admin", __name__, url_prefix='/admin')


@bp.route('/')
def admin():
    return render_template('admin/home.html')


@bp.route('/presence')
def presence():
    return render_template('admin/presence.html')
