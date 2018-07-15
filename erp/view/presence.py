from flask import Blueprint, render_template
from erp.model import Absence

bp = Blueprint("presence", __name__, url_prefix='/admin/presence')


@bp.route('/')
def presence_view():
    absences = Absence.query.all()

    return render_template(
        'admin/presence.html',
        absences=absences
    )
