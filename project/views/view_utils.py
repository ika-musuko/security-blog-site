import random
from functools import wraps

from flask import request, url_for, flash, session
from werkzeug.utils import redirect

import datetime

from project import app, POSTS_PER_PAGE
from project.models import posts_model
from project.users import sessions, auth
from project.utils import random_string

GETPOST = ['GET', 'POST']
GET = ['GET']
POST = ['POST']

# template variable injections
@app.context_processor
def inject_posts_per_page():
    return dict(POSTS_PER_PAGE=POSTS_PER_PAGE)

@app.context_processor
def inject_login_session():
    return dict(current_user_id=sessions.current_user_id())

@app.context_processor
def inject_current_user():
    return dict(current_user=sessions.current_user())

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
        if not sessions.current_user_id():
            flash("You must login to access this content.")
            return redirect(url_for("index"))

        return f(*args, **kwargs)
    return inside

def logout_required(f):
    @wraps(f)
    def inside(*args, **kwargs):
        if sessions.current_user_id():
            flash("You are already logged in.")
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return inside


def email_unverified(f):
    @wraps(f)
    def inside(*args, **kwargs):
        if auth.is_email_verified(sessions.current_user_id()):
            flash("You have already verified your email.")
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return inside

def email_verified(f):
    @wraps(f)
    def inside(*args, **kwargs):
        if not auth.is_email_verified(sessions.current_user_id()):
            flash("Please verify your email before accessing this content.")
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return inside


def admin_user(f):
    @wraps(f)
    def inside(*args, **kwargs):
        cu = sessions.current_user()
        if cu['role'] != 'admin':
            flash("You must be an admin to access this content.")
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return inside


def god_user(f):
    @wraps(f)
    def inside(*args, **kwargs):
        cid = sessions.current_user_id()
        if cid !="sherwyn" and cid != "cs166_admin":
            flash("You are not authorized to do this.")
            return redirect(request.referrer)
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


def paginate_posts(page: int=1, user_id: int=None):
    posts = posts_model.query_posts(start=page * POSTS_PER_PAGE, end=(page - 1) * POSTS_PER_PAGE, user_id=user_id)
    total_posts = posts_model.get_total_posts()
    return posts, total_posts