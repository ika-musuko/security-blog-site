'''
normal_views.py

routes for the normal views
'''

from flask import redirect, url_for, render_template
import string
import random
import datetime

from project import app, POSTS_PER_PAGE

def random_string(length: int):
    return ''.join([random.choice(string.ascii_lowercase) for _ in range(length)])

def postmaker(total_posts: int, page: int):
    total_posts = 41

    posts = [{
        "id": i+1
        ,"title": random_string(8)
        ,"author": random_string(13)
        ,"published_on": datetime.datetime.today()
        ,"preview": random_string(random.randint(50,125))
    } for i in range(total_posts)]

    # array indexing starts on 0
    ppage = page - 1
    return posts[ppage*POSTS_PER_PAGE:page*POSTS_PER_PAGE]

@app.route('/')
@app.route('/index/')
@app.route('/index/<int:page>')
def index(page: int=1):
    # query the database for page*POSTS_PER_PAGE ~ (page+1)*POSTS_PER_PAGE
    #todo
    total_posts = 41
    posts = postmaker(total_posts, page)

    return render_template("index.html", total_posts=total_posts, posts=posts, page=page)


@app.route("/new_post")
def new_post():
    return "new post"

@app.route("/your_profile")
def your_profile():
    # redirect to current user's profile page
    return redirect(url_for("profile", username="username", page=1))


@app.route("/profile/<username>")
def profile(username: str):
    user = {
          "join_date" : datetime.datetime.today()
        , "admin_status" : True
    }
    return render_template("profile.html", username=username, user=user)

@app.route("/demos")
def demos():
    return render_template("demos.html")


@app.route("/post/<int:number>")
def post(number: int):
    return "post: %s" % number



@app.route("/edit_post/<int:number>")
def edit_post(number: int):
    return "EDIT post: %s" % number


@app.route("/delete_post/<int:number>")
def delete_post(number: int):
    return "DELETE post: %s" % number


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")
