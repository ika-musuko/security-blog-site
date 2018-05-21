from flask import render_template, request, flash
from project.views.view_utils import GETPOST
from project import app
from project.models import naive_code

@app.route("/demos", methods=GETPOST)
def demos():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        password = request.form.get("password")

        result = naive_code.verify_login_insecure(user_id, password)
        if result:
            flash("The credentials for %s are correct!" % (user_id))
        else:
            flash("Incorrect credentials...")

    return render_template("demos.html")