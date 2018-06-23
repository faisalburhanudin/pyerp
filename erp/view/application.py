from flask import Blueprint, render_template
from erp.model import Application

bp = Blueprint("application", __name__, url_prefix='/admin/application')


@bp.route('/')
def get_applications():
    applications = Application.query.all()
    return render_template(
        'admin/application/list.html',
        applications=applications
    )