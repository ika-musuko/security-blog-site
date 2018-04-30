'''
error_views.py

routes for error pages
'''

from project import app


@app.errorhandler(401)
def unauthorized_error():
    return "401 not authorized"


@app.errorhandler(404)
def not_found_error():
    return "404 not found"


@app.errorhandler(500)
def internal_server_error():
    return "500 internal server error"
