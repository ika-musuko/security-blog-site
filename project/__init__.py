from flask import Flask

# app initialization
app = Flask(__name__)
app.secret_key = "ReallyGoodS3cur1tyblogsite" # this must be set so sessions can be used

# global constants
POSTS_PER_PAGE = 5


from project.views import auth_views, normal_views, error_views, view_utils
