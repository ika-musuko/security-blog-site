from flask import render_template, url_for, request, flash
from werkzeug.utils import redirect

from project import utils
import project.exceptions.user_exceptions
import project.users.auth
from project import app, recaptcha
from project.users import sessions
from project.views.view_utils import GETPOST, login_required, logout_required, email_unverified
from project.utils import check_valid_password
from project.models import users_model

from time import sleep


@app.route("/login", methods=GETPOST)
@logout_required
def login():

    if request.method == "POST":

        # get the form data
        username = request.form.get("username")
        password = request.form.get("password")
        remember_me = request.form.get("remember_me")

        if sessions.login_user(username, password, remember_me):
            flash("You have successfully logged in as %s" % (username))
            return redirect(url_for("index"))

        # login failed
        sleep(5) # make failed users wait
        flash("Your credentials are incorrect.")

    return render_template("login.html")


@app.route("/register", methods=GETPOST)
@logout_required
def register():

    if request.method == "POST":
        if recaptcha.verify():
            # get the form data
            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")
            confirm_password = request.form.get("confirm_password")

            # form verification
            if not utils.check_valid_email_address(email):
                flash("Please input a valid email address")
                return redirect(url_for("register"))

            if any(len(field) == 0 for field in (username, email, password, confirm_password)):
                flash("You cannot leave any of the fields blank.")
                return redirect(url_for("register"))

            if password != confirm_password:
                flash("The password and confirm password fields must be the same.")
                return redirect(url_for("register"))

            # password verification
            if not check_valid_password(password):
                flash("This password is not valid. It must meet the following criteria: 8 more characters, contain both upper and lowercase letters, contain a number, and contain a symbol")
                return redirect(url_for("register"))

            # send information to be verified on the database
            if users_model.create_new_user(username, email, password):
                flash("Thanks for signing up! Please check your email for a verification link.")
                project.users.auth.send_email_verification(username)
                sessions.login_user(username, password)
                return redirect(url_for("index"))

            else:
                flash("This user already exists. Please use a different username")
                return redirect(url_for("register"))

        else:
            flash("ReCaptcha verification unsuccessful. Are you a robot?")

    return render_template("register.html")

@app.route("/resend_verification", methods=GETPOST)
@login_required
@email_unverified
def resend_verification():
    cu = sessions.current_user()
    project.users.auth.send_email_verification(cu['user_id'])
    email_censored = utils.censor_email(cu['email'])
    flash("Email verification re-sent to %s" % email_censored)
    return redirect(url_for("index"))

@app.route("/logout", methods=GETPOST)
@login_required
def logout():
    sessions.logout_user()
    return redirect(url_for("index"))


@app.route("/verify/<username>/<verification_str>", methods=GETPOST)
def verify(username: str, verification_str: str):
    try:
        project.users.auth.verify_registration(username, verification_str)
        flash("You have verified your email! You may log in now")
        return redirect(url_for("login"))

    except project.exceptions.user_exceptions.InvalidVerification:
        flash("This is not a valid verification URL. Email has been resent.")
        project.users.auth.send_email_verification(username)
        return redirect(url_for("index"))

    except project.exceptions.user_exceptions.EmailAlreadyVerified:
        flash("You have already verified your email.")
        return redirect(url_for("index"))

