import hashlib

from flask import url_for

from project import email, models
from project.exceptions.user_exceptions import EmailAlreadyVerified, InvalidVerification
from project.models.users_model import get_email_verification


def verify_login(username: str, password: str):
    pass


def hash_password(password, salt):
    '''
    hash a password with a salt
    :param password:
    :param salt:
    :return:
    '''
    hash_object = hashlib.sha224(bytes(''.join((password, salt))))
    return hash_object.hexdigest()


def send_email_verification(user_id: str):
    verification_str = get_email_verification()
    verification_url = url_for("verify", user_id=user_id, verification_str=verification_str)


    return email.send_email("Thank you for registering for Sherwyn's CS 166 Security Blog! Go to the following link to verify your email: %s" % verification_url)


def verify_registration(user_id: str, url_string: str):
    # get the email verification string stored on the database
    user_email_ver = get_email_verification(user_id)

    # if there's nothing in the email_verified field, that means the user already registered
    if not user_email_ver:
        raise EmailAlreadyVerified

    # if the url string and the database field don't match, then it's not valid
    if url_string != user_email_ver:
        raise InvalidVerification

    # if the string is correct, set the database string to None to verify the user
    models.set_sql("UPDATE users SET email_verification=NULL WHERE user_id=%s", [user_id])