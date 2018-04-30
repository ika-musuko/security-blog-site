from project import app

from flask import redirect, url_for


@app.route('/')
def index():
    return "hi"


@app.route("/demos")
def demos():
    return "demos"


@app.route("/login")
def login():
    return "login"


@app.route("/register")
def register():
    return "register"


@app.route("/logout")
def logout():
    redirect(url_for("index"))


@app.route("/post/<int:number>")
def post(number: int):
    return "post: %s" % number


@app.route("/privacy")
def privacy():
    return "privacy statement"

