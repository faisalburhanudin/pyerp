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


@bp.route('/edit-reward', methods=["POST", "GET"])
def edit_reward():
    if request.method == "POST":
        reward_id = request.form.get("id")
        name = request.form.get("name")

        reward = RewardPunish.query.filter_by(id=reward_id).first()
        reward.name = name

        db.session.add(reward)
        db.session.commit()

        return redirect('/admin/reward-punish')

    reward_id = request.args.get("id")
    reward = RewardPunish.query.filter_by(id=reward_id).first()

    return render_template(
        'admin/reward_and_punish/edit_reward.html',
        reward=reward
    )


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
