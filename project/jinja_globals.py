from project.utils import random_string


def csrf_token():
    return random_string(length=64)



JINJA_GLOBALS = {
    "csrf_token" : csrf_token
}
