'''
normal_views.py

routes for the normal views
'''

from flask import render_template, url_for, redirect

from project import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/demos")
def demos():
    return render_template("demos.html")

@app.route("/your_profile")
def your_profile():
    return "your profile"

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
