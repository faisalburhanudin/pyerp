import datetime

from flask import Blueprint, render_template, request

from erp.model import Application, db

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
