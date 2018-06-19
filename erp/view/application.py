from flask import Blueprint, render_template

bp = Blueprint('application', __name__)


@bp.route('/')
def form_application():
    return render_template('form-application.html')
