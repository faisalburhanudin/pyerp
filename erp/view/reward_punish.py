from flask import render_template, Blueprint, request, redirect

from erp.model import Users, RewardPunish, db, UserRewardPunish

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


@bp.route('/user-reward', methods=["POST", "GET"])
def add_user_reward():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        reward_id = request.form.get("reward_id")

        user_reward = UserRewardPunish()
        user_reward.user_id = user_id
        user_reward.reward_punish_id = reward_id

        db.session.add(user_reward)
        db.session.commit()

        return redirect('/admin/reward-punish')

    user_id = request.args.get("id")
    user = Users.query.filter_by(id=user_id).first()
    rewards = RewardPunish.query.filter_by(type=1).all()

    return render_template(
        'admin/reward_and_punish/user_reward.html',
        user=user,
        rewards=rewards
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


@bp.route('/edit-punish', methods=["GET", "POST"])
def edit_punish():
    if request.method == "POST":
        punish_id = request.form.get("id")
        name = request.form.get("name")

        punish = RewardPunish.query.filter_by(id=punish_id).first()
        punish.name = name

        db.session.add(punish)
        db.session.commit()

        return redirect("/admin/reward-punish")

    punish_id = request.args.get("id")
    punish = RewardPunish.query.filter_by(id=punish_id).first()
    return render_template(
        'admin/reward_and_punish/edit_punish.html',
        punish=punish
    )


@bp.route('/user-punish', methods=["POST", "GET"])
def add_user_punish():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        punish_id = request.form.get("punish_id")

        user_punish = UserRewardPunish()
        user_punish.user_id = user_id
        user_punish.reward_punish_id = punish_id

        db.session.add(user_punish)
        db.session.commit()

        return redirect('/admin/reward-punish')

    user_id = request.args.get("id")
    user = Users.query.filter_by(id=user_id).first()
    punish = RewardPunish.query.filter_by(type=2).all()

    return render_template(
        'admin/reward_and_punish/user_punish.html',
        user=user,
        punish=punish
    )
