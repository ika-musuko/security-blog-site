from project import models
from project.exceptions.user_exceptions import UserExistsException
from project.users.auth import hash_password
from project.utils import generate_random_string
import datetime


def check_user_exists(user_id: str):
    '''
    check if the user exists in the database
    :param user_id:
    :return:
    '''
    return models.get_sql_simple("SELECT COUNT(user_id) FROM users;", amount=1) > 0


def create_new_user(user_id: str, email: str, password: str):
    '''
    create a new user on the database or blow out with an exception if they already exist
    :param user_id:
    :param email:
    :param password:
    :return:
    '''
    if check_user_exists(user_id):
        raise UserExistsException

    # create a password salt for this user
    password_salt = generate_random_string(250)

    # hash the user's password with the salt
    password_hash = hash_password(password, password_salt)

    # create a random string for the email verification
    email_verification = generate_random_string(250)

    # add the user into the database
    models.add_row(table="users", data = {
          "user_id" : user_id
        , "join_date" : datetime.datetime.now()
        , "password_hash" : password_hash
        , "password_salt" : password_salt
        , "email" : email
        , "role" : "user"
        , "email_verification" : email_verification
    })


def get_email_verification(user_id: str):
    return models.get_sql(statement="SELECT email_verification FROM users WHERE user_id=%s", values=[user_id], amount=1)["email_verification"]


def is_email_verified(user_id: str):
    '''
    basically, if the email verification string is None for the user, their email is verified
    :param user_id:
    :return:
    '''
    return not get_email_verification(user_id)