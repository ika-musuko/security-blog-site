'''
normal_views.py

routes for the normal views
'''

from flask import redirect, url_for, render_template
import datetime

from project import app
from project.views.view_utils import login_required, email_verified, postmaker


@app.route('/')
@app.route('/index/')
@app.route('/index/<int:page>')
def index(page: int=1):
    # query the database for page*POSTS_PER_PAGE ~ (page+1)*POSTS_PER_PAGE
    #todo
    total_posts = 41
    posts = postmaker(total_posts, page)

    return render_template("index.html", total_posts=total_posts, posts=posts, page=page)



@app.route("/your_profile")
@login_required
def your_profile():
    # redirect to current user's profile page
    return redirect(url_for("profile", username="username", page=1))


@app.route("/profile/<username>")
def profile(username: str):
    user = {
          "join_date" : datetime.datetime.today()
        , "email_verified": True
        , "admin_status" : True
    }
    return render_template("profile.html", username=username, user=user)

@app.route("/demos")
def demos():
    return render_template("demos.html")


@app.route("/post/<int:number>")
def post(number: int):
    return "post: %s" % number


@app.route("/new_post")
@login_required
@email_verified
def new_post():
    return "new post"

@app.route("/edit_post/<int:number>")
@login_required
@email_verified
def edit_post(number: int):
    return "EDIT post: %s" % number


@app.route("/delete_post/<int:number>")
@login_required
@email_verified
def delete_post(number: int):
    return "DELETE post: %s" % number


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")
