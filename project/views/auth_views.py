from flask import render_template, url_for
from werkzeug.utils import redirect

from project import app


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/logout")
def logout():
    return redirect(url_for("index"))