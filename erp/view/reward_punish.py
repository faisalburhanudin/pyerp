from flask import render_template, Blueprint, request, redirect

from erp.model import Users, RewardPunish, db

bp = Blueprint('reward_punish', __name__, url_prefix='/admin/reward-punish')


@bp.route('/')
def reward_and_punishment():
    users = Users.query.all()
    return render_template(
        'admin/reward-and-punish/list.html',
        users=users
    )


@bp.route('/add-reward', methods=["GET", "POST"])
def add_reward():
    if request.method == "POST":
        name = request.form.get("name")

        rp = RewardPunish()
        rp.name = name

        db.session.add(rp)
        db.session.commit()

        return redirect("/admin/reward-punish")

    return render_template('admin/reward-and-punish/add-reward.html')


@bp.route('/add-punish')
def add_punish():
    return render_template('admin/reward-and-punish/add-punish.html')
