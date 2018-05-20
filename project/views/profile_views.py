from flask import url_for, render_template, flash, redirect
from werkzeug.utils import redirect

from project import app
from project.models import users_model
from project.users import sessions
from project.views.view_utils import login_required, admin_user, god_user


@app.route("/all_users")
def all_users():
    every_user = users_model.get_all_users(["user_id", "join_date", "role"])
    return render_template("all_users.html", users=every_user)


@app.route("/your_profile")
@login_required
def your_profile():
    # redirect to current user's profile page
    return redirect(url_for("profile", username=sessions.current_user_id(), page=1))


@app.route("/profile/<username>")
def profile(username: str):
    #user = {
    #      "join_date" : datetime.datetime.today()
    #    , "email_verified": True
    #    , "admin_status" : True
    #}
    user = users_model.get_user(username)
    # if the user exists, show their profile
    if user:
        #user_posts = posts_model.get_user_posts(username)

        return render_template("profile.html", username=username, user=user)
    flash("User %s does not exist." % username)
    return redirect(url_for("index"))

@app.route("/toggle_admin_status/<username>")
@god_user
def toggle_admin_status(username: str):
    role = users_model.get_user(username, ["role"])["role"]
    new_role = "admin" if role == "user" else "user"
    users_model.set_user(username, "role", new_role)
    flash("%s's role is now set to: %s" % (username, new_role))
    return redirect(url_for("profile", username=username))