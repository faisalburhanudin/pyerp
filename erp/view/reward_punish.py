from flask import render_template, Blueprint, request, redirect

from erp.model import Users, RewardPunish, db

bp = Blueprint('reward_punish', __name__, url_prefix='/admin/reward-punish')


@bp.route('/')
def reward_and_punishment():
    users = Users.query.all()
    rewards = RewardPunish.query.filter_by(type=1).all()
    punishments = RewardPunish.query.filter_by(type=2).all()

    return render_template(
        'admin/reward_and_punish/list.html',
        users=users,
        rewards=rewards,
        punishments=punishments
    )


@bp.route('/add-reward', methods=["GET", "POST"])
def add_reward():
    if request.method == "POST":
        name = request.form.get("name")

        rp = RewardPunish()
        rp.name = name
        rp.type = 1

        db.session.add(rp)
        db.session.commit()

        return redirect("/admin/reward-punish")

    return render_template('admin/reward_and_punish/add_reward.html')


@bp.route('/add-punish', methods=['GET', 'POST'])
def add_punish():
    if request.method == "POST":
        name = request.form.get("name")

        rp = RewardPunish()
        rp.name = name
        rp.type = 2

        db.session.add(rp)
        db.session.commit()

        return redirect("/admin/reward-punish")

    return render_template('admin/reward_and_punish/add_punish.html')
