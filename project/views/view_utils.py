import random
from functools import wraps

from flask import request, url_for, flash, session
from werkzeug.utils import redirect

import datetime

from project import app, POSTS_PER_PAGE
from project.users import sessions, auth
from project.utils import random_string

GETPOST = ['GET', 'POST']
GET = ['GET']
POST = ['POST']

@app.context_processor
def inject_posts_per_page():
    return dict(POSTS_PER_PAGE=POSTS_PER_PAGE)

# set cookies on every request
@app.after_request
def set_cookie(resp):
    resp.set_cookie(key="last_here", value=str(datetime.datetime.now()))
    resp.set_cookie(key="last_page", value=request.base_url)

    print(session)
    return resp

# decorators
def post_searcher(f):
    '''
    use this decorator for any page that utilizes the search bar
    :param f:
    :return:
    '''
    @wraps(f)
    def inside(*args, **kwargs):
        if request.method == "POST" and request.form["search"]:
            keyword = request.form["search"]
            return redirect(url_for("search", keyword=keyword))
        return f(*args, **kwargs)
    return inside

def login_required(f):
    @wraps(f)
    def inside(*args, **kwargs):
        if not sessions.current_user():
            flash("You must login to access this content.")
            return redirect(url_for("index"))

        return f(*args, **kwargs)
    return inside

def logout_required(f):
    @wraps(f)
    def inside(*args, **kwargs):
        if sessions.current_user():
            flash("You are already logged in.")
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return inside


def email_unverified(f):
    @wraps(f)
    def inside(*args, **kwargs):
        if not auth.is_email_verified(sessions.current_user()):
            flash("Please verify your email before accessing this content.")
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return inside

def email_verified(f):
    @wraps(f)
    def inside(*args, **kwargs):
        if auth.is_email_verified(sessions.current_user()):
            flash("You have already verified your email.")
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return inside


def admin_user(f):
    @wraps(f)
    def inside(*args, **kwargs):
        #todo: check if the user is an admin
        return f(*args, **kwargs)
    return inside



# other helpers
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


