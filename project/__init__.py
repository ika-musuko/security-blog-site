from flask import Flask
app = Flask(__name__)
POSTS_PER_PAGE = 5


from project.views import auth_views, normal_views, error_views, view_utils
