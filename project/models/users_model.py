from project import models
from project.exceptions.user_exceptions import UserExistsException
from project.utils import random_string, hash_password, comma_join
import datetime


def get_user(username: str, columns: list=None):
    columns_formatted = comma_join(columns) if columns else '*'
    return models.get_sql(statement="SELECT {} FROM users WHERE user_id=%s".format(columns_formatted), values=[username], amount=1)

def set_user(username: str, column: str, value):
    models.set_sql("UPDATE users SET {}=%s WHERE user_id=%s".format(column), [value, username])

def check_user_exists(user_id: str):
    '''
    check if the user exists in the database
    :param user_id:
    :return:
    '''
    return models.get_sql("SELECT COUNT(user_id) FROM users WHERE user_id=%s;", values=[user_id], amount=1)["COUNT(user_id)"] > 0


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
    password_salt = random_string(30)

    # hash the user's password with the salt
    password_hash = hash_password(password, password_salt)

    # create a random string for the email verification
    email_verification = random_string(250)

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
    return get_user(user_id, ["email_verification"])["email_verification"]

