from flask import render_template, url_for, request, flash
from werkzeug.utils import redirect

import project.exceptions.user_exceptions
import project.users.auth
from project import app, recaptcha
from project.users import sessions
from project.views.view_utils import GETPOST, login_required, logout_required
from project.models import users_model

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
            try:
                if users_model.create_new_user(username, email, password):
                    flash("Thanks for signing up! Please verify your email and log in.")
                    project.users.auth.send_email_verification(username)
                    return redirect(url_for("index"))

            except project.exceptions.user_exceptions.UserExistsException:
                flash("This user already exists. Please use a different username")
                return redirect(url_for("register"))

        else:
            flash("ReCaptcha verification unsuccessful. Are you a robot?")

    return render_template("register.html")


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

def check_valid_password(password: str) -> bool:

    # check each condition individually to prevent linearization attack
    password_conditions = [
          len(password) > 7
        , not (not any(c.isupper() for c in password)) # make sure that every character is checked and no short circuit happens
        , not (not any(c.islower() for c in password))
        , not (not any(c.isnumeric() for c in password))
        , not (not any(c in "!@#$%^&*" for c in password))
    ]
    return all(password_conditions) # if all conditions are true