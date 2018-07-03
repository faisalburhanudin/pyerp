import datetime

from sqlalchemy import func
from flask import Blueprint, render_template, request, redirect

from erp.model import Application, Users, db, Absence

bp = Blueprint('home', __name__)


@bp.route('/', methods=["POST", "GET"])
def form_application():
    if request.method == "POST":
        name = request.form.get("name")
        photo = request.files.get("photo")
        email = request.form.get("email")
        year_experience = request.form.get("year_experience")
        birthday = request.form.get("birthday")
        birthday = datetime.datetime.strptime(birthday, '%m/%d/%Y').strftime('%Y-%m/%d')
        resume = request.files.get("resume")

        app = Application()
        app.name = name
        app.set_photo(file=photo)
        app.email = email
        app.year_experience = year_experience
        app.birthday = birthday
        app.set_resume(file=resume)

        db.session.add(app)
        db.session.commit()

    return render_template('form-application.html')


@bp.route('/absence', methods=["POST", "GET"])
def form_absence():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = Users.query.filter_by(email=email).first()

        if not user.validate_password(password):
            return redirect('/absence')

        absence = Absence()
        absence.user_id = user.id
        absence.date_time = datetime.datetime.now()

        db.session.add(absence)
        db.session.commit()

        return redirect(f'/absence/{ user.id }')

    return render_template('form-absence.html')


@bp.route('/absence/<user_id>')
def absence_list(user_id):
    month = request.args.get("month")

    if not month:
        today = datetime.datetime.today()
        month = today.month

    absences = Absence.query.filter(
        Absence.user_id == user_id,
        func.MONTH(Absence.date_time) == month
    ).all()

    user = Users.query.filter_by(id=user_id).first()

    return render_template(
        'absences.html',
        user=user,
        absences=absences
    )
