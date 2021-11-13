from .import bp as social
from flask import render_template, flash, redirect, url_for
from app.models import User
from flask_login import login_required, current_user

@social.route('/show_users')
@login_required
def show_users():
    users = User.query.all()
    return render_template('show_users.html.j2', users= users)

# @social.route('/follow/<int:id>') 
# @login_required
# def follow(id):
#     user_to_follow = User.query.get(id)
#     current_user.follow(user_to_follow)
#     flash(f" you are now following {user_to_follow.first_name} {user_to_follow.last_name}",'success')
#     return redirect(url_for('social.show_users'))

# @social.route('/unfollow/<int:id>') 
# @login_required
# def follow(id):
#     user_to_unfollow = User.query.get(id)
#     current_user.follow(user_to_unfollow)
#     flash(f" you are now unfollowing {user_to_unfollow.first_name} {user_to_unfollow.last_name}",'warning')
#     return redirect(url_for('social.show_users'))    


