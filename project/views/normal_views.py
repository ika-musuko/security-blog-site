'''
normal_views.py

routes for the normal views
'''

from flask import request, redirect, url_for, render_template
import datetime

from project import app, POSTS_PER_PAGE
from project.views.view_utils import GETPOST, post_searcher, login_required, email_verified, postmaker

from project import models


@app.route('/', methods=GETPOST)
@app.route('/index/', methods=GETPOST)
@app.route('/index/<int:page>', methods=GETPOST)
@post_searcher
def index(page: int=1):
    # query the database for page*POSTS_PER_PAGE ~ (page+1)*POSTS_PER_PAGE
    total_posts = 41
    posts = postmaker(total_posts, page)
    #posts = models.query_posts(start=page*POSTS_PER_PAGE, end=(page-1)*POSTS_PER_PAGE)
    #total_posts = models.get_total_posts()
    return render_template("index.html", total_posts=total_posts, posts=posts, page=page)

@app.route('/search/<keyword>', methods=GETPOST)
@app.route('/search/<keyword>/<int:page>', methods=GETPOST)
@post_searcher
def search(keyword: str, page: int=1):
    # query the database for page*POSTS_PER_PAGE ~ (page+1)*POSTS_PER_PAGE
    #todo
    total_posts = 21
    posts = postmaker(total_posts, page)

    return render_template("search.html", keyword=keyword, total_posts=total_posts, posts=posts, page=page)


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


@app.route("/new_post", methods=GETPOST)
@login_required
@email_verified
def new_post():
    return render_template("new_post.html")

@app.route("/edit_post/<int:number>")
@login_required
@email_verified
def edit_post(number: int):
    return render_template("edit_post.html", number=number)


@app.route("/delete_post/<int:number>")
@login_required
@email_verified
def delete_post(number: int):
    return "DELETE post: %s" % number


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")
