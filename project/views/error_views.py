'''
error_views.py

routes for error pages
'''

from project import app


@app.errorhandler(401)
def unauthorized_error(e):
    return "401 not authorized", 401


@app.errorhandler(404)
def not_found_error(e):
    return "404 not found", 404


@app.errorhandler(500)
def internal_server_error(e):
    return "500 internal server error", 500
