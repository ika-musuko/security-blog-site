from flask import render_template, url_for
from werkzeug.utils import redirect

from project import app
from project.views.view_utils import GETPOST, email_unverified, login_required, logout_required

@app.route("/login", methods=GETPOST)
@logout_required
def login():
    return render_template("login.html")


@app.route("/register", methods=GETPOST)
@logout_required
def register():
    return render_template("register.html")


@app.route("/resend_email_verification", methods=GETPOST)
@login_required
@email_unverified
def resend_email_verification():
    return "resend email verification"

@app.route("/logout", methods=GETPOST)
@login_required
def logout():
    return redirect(url_for("index"))