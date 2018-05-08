import datetime
import random
import string

from project import app, POSTS_PER_PAGE

@app.context_processor
def inject_posts_per_page():
    return dict(POSTS_PER_PAGE=POSTS_PER_PAGE)


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