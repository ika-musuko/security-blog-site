from project.utils import generate_random_string


def csrf_token():
    return generate_random_string(length=64)



JINJA_GLOBALS = {
    "csrf_token" : csrf_token
}
