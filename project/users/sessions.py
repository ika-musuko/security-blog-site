from flask import session, request
from project.users.auth import verify_login


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
        session['remember_me'] = True


def logout_user():
    # remove the user from the session
    session.pop(current_user(), None)


def current_user():
    return session['user_id'] if 'user_id' in session else None