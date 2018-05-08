'''
normal_views.py

routes for the normal views
'''

from flask import render_template

from project import app, POSTS_PER_PAGE

@app.route('/')
@app.route('/index/')
@app.route('/index/<int:page>')
def index(page: int=1):
    # query the database for page*POSTS_PER_PAGE ~ (page+1)*POSTS_PER_PAGE
    #todo

    posts = [
         {
              "title": "wow"
            , "author": "wowcool"
            , "published_on" : "Today"
            , "preview" : "Oh yeah...wow"

         }
        ,{
              "title": "Great"
            , "author": "greatdude250"
            , "published_on" : "Yesterday"
            , "preview" : "Super great!"

        }
        ,{
              "title": "I'm so awesome!"
            , "author": "awesome_man_1"
            , "published_on" : "Today"
            , "preview" : "I am the most awesome man!"

         }
    ]*3

    for i, post in enumerate(posts):
        print(i)
        post["id"] = i

    print(*(post["id"]))

    # array indexing starts on 0
    ppage = page - 1
    total_posts = len(posts)
    print(ppage*POSTS_PER_PAGE, page*POSTS_PER_PAGE)
    #posts = posts[ppage*POSTS_PER_PAGE:page*POSTS_PER_PAGE]
    posts = posts[0:10]
    print(posts)

    return render_template("index.html", total_posts=total_posts, posts=posts, page=page)


@app.route("/demos")
def demos():
    return render_template("demos.html")

@app.route("/your_profile")
def your_profile():
    return "your profile"


@app.route("/post/<int:number>")
def post(number: int):
    return "post: %s" % number


@app.route("/privacy")
def privacy():
    return "privacy statement"
