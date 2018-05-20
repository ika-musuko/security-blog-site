from project import jinja_globals
from flask import Flask
from flask_recaptcha import ReCaptcha
import pymysql
import os

# app initialization
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY") or '' # this must be set so sessions can be used

# pymysql initialization
PYMYSQL_CONFIG = {
    'host':          os.getenv("PYMYSQL_HOST") or ''
    ,'user':          os.getenv("PYMYSQL_USER") or ''
    ,'password':          os.getenv("PYMYSQL_PASSWORD") or ''
    ,'db':          os.getenv("PYMYSQL_DB") or ''
    ,'charset':          'utf8mb4'
    ,'cursorclass':          pymysql.cursors.DictCursor
}

# global constants
POSTS_PER_PAGE = 5

# recaptcha initialization
recaptcha = ReCaptcha()
recaptcha.init_app(app)


# global jinja functions
app.jinja_env.globals.update(**jinja_globals.JINJA_GLOBALS)

from project.views import auth_views, normal_views, error_views, view_utils
