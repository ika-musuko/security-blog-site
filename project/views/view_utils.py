import datetime
import random
import string
from functools import wraps

from flask import request, url_for
from werkzeug.utils import redirect

from project import app, POSTS_PER_PAGE

GETPOST = ['GET', 'POST']
GET = ['GET']
POST = ['POST']

@app.context_processor
def inject_posts_per_page():
    return dict(POSTS_PER_PAGE=POSTS_PER_PAGE)

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
        #todo: check if the user is logged in
        return f(*args, **kwargs)
    return inside

def logout_required(f):
    @wraps(f)
    def inside(*args, **kwargs):
        #todo: check if the user is logged out
        return f(*args, **kwargs)
    return inside


def email_unverified(f):
    @wraps(f)
    def inside(*args, **kwargs):
        #todo: check if the user has NOT verified their email
        return f(*args, **kwargs)
    return inside

def email_verified(f):
    @wraps(f)
    def inside(*args, **kwargs):
        #todo: check if the user has verified their email
        return f(*args, **kwargs)
    return inside


def admin_user(f):
    @wraps(f)
    def inside(*args, **kwargs):
        #todo: check if the user is an admin
        return f(*args, **kwargs)
    return inside



# other helpers
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


