from flask import url_for

from project import email
from project.exceptions.user_exceptions import EmailAlreadyVerified, InvalidVerification
from project.models import users_model
from project.models.users_model import get_email_verification
from project.utils import hash_password


def verify_login(username: str, password: str):
    user = users_model.get_user(username)
    if not user:
        return False
    inputted_password_hash = hash_password(password, user["password_salt"])
    return inputted_password_hash == user["password_hash"]


def send_email_verification(user_id: str):
    user = users_model.get_user(user_id, ["email_verification", "email"])
    verification_str = user["email_verification"]
    try:
        verification_url = url_for("verify", username=user_id, verification_str=verification_str, _external=True)
    except RuntimeError:
        verification_url = "SENT FROM TERMINAL: %s" % (verification_str)

    return email.send_email("Thank you for registering for Sherwyn's CS 166 Security Blog! Go to the following link to verify your email: %s" % verification_url, user["email"])


def verify_registration(user_id: str, url_string: str):
    # get the email verification string stored on the database
    user_email_ver = users_model.get_email_verification(user_id)

    # if there's nothing in the email_verified field, that means the user already registered
    if not user_email_ver:
        raise EmailAlreadyVerified

    # if the url string and the database field don't match, then it's not valid
    if url_string != user_email_ver:
        raise InvalidVerification

    # if the string is correct, set the database string to None to verify the user
    users_model.set_user(user_id, "email_verification", None)


def is_email_verified(user_id: str):
    '''
    basically, if the email verification string is None for the user, their email is verified
    :param user_id:
    :return:
    '''
    return not get_email_verification(user_id)