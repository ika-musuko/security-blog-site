from flask import session
from project import models
import datetime

class UserException(Exception):
    pass

class UserExistsException:
    pass


def login_user(username: str, password: str, remember_me: bool) -> bool:
    '''
    check if the user's credentials are correct and then store their info to a session

    :param username:
    :param password:
    :param remember_me:
    :return:
    '''
    if not verify_login(username, password):
        return False

    # now store the data to the session
    session['user_id'] = username
    if remember_me:
        session['remember_me'] = 'set'




def check_user_exists(user_id: str):
    '''
    check if the user exists in the database
    :param user_id:
    :return:
    '''
    return models.get_sql("SELECT COUNT(user_id) FROM users;", amount=1) > 0

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



def send_email_verification(user_id: str):
    return "EMAIL VERIFICATION STRING"