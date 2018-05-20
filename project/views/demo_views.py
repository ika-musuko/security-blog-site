from flask import render_template

from project import app


@app.route("/demos")
def demos():
    return render_template("demos.html")