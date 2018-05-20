'''
post_views.py

routes for the normal views
'''

from flask import redirect, url_for, render_template, flash, request

from project.models import posts_model
from project import app, POSTS_PER_PAGE
from project.views.view_utils import GETPOST, login_required, email_verified, postmaker
from project.users import sessions


def paginate_posts(page: int=1):
    posts = posts_model.query_posts(start=page * POSTS_PER_PAGE, end=(page - 1) * POSTS_PER_PAGE)
    total_posts = posts_model.get_total_posts()
    return posts, total_posts

@app.route('/', methods=GETPOST)
@app.route('/index/', methods=GETPOST)
@app.route('/index/<int:page>', methods=GETPOST)
def index(page: int=1):
    # query the database for page*POSTS_PER_PAGE ~ (page+1)*POSTS_PER_PAGE
    #total_posts = 41
    #posts = postmaker(total_posts, page)
    posts, total_posts = paginate_posts(page)
    return render_template("index.html", total_posts=total_posts, posts=posts, page=page)

@app.route('/search/<keyword>', methods=GETPOST)
@app.route('/search/<keyword>/<int:page>', methods=GETPOST)
def search(keyword: str, page: int=1):
    # query the database for page*POSTS_PER_PAGE ~ (page+1)*POSTS_PER_PAGE
    #todo
    total_posts = 21
    posts = postmaker(total_posts, page)

    return render_template("search.html", keyword=keyword, total_posts=total_posts, posts=posts, page=page)


@app.route("/post/<int:number>")
def post(number: int):
    post = posts_model.get_post(post_id=number)
    # the post does exist
    if post:
        return render_template("post.html", number=number, post=post)
    # the post does not exist
    flash("Post %s does not exist" % number)
    return redirect(url_for("index"))

@app.route("/new_post", methods=GETPOST)
@login_required
@email_verified
def new_post():
    title = ''
    content = ''
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")

        if not title:
            flash("Please title your post.")
            return redirect(url_for("new_post", title=title, content=content))

        if not content:
            flash("Please write some content.")
            return redirect(url_for("new_post", title=title, content=content))

        posts_model.add_post(sessions.current_user_id(), title, content)
        flash("Your post has been submitted.")
        return redirect(url_for('index'))


    return render_template("new_post.html", title=title, content=content)

@app.route("/edit_post/<int:number>")
@login_required
@email_verified
def edit_post(number: int):
    return render_template("edit_post.html", number=number)


@app.route("/delete_post/<int:number>")
@login_required
@email_verified
def delete_post(number: int):
    cu = sessions.current_user()
    post = posts_model.get_post(number)
    if cu['role'] != 'admin' and cu['user_id'] != post['user_id']:
        flash("You may not delete this post.")

    else:
        posts_model.delete_post(number)

    return redirect(url_for("index"))


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")
