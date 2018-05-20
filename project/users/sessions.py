from flask import session, request
from project.users.auth import verify_login
from project.models import users_model


def login_user(username: str, password: str, remember_me: bool=False) -> bool:
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
    return True


def logout_user():
    # remove the user from the session
    session.clear()


def current_user_id():
    return session['user_id'] if 'user_id' in session else None

def current_user():
    # No user is logged in
    cid = current_user_id()
    if not cid:
        return None

    # get the user's information from the database
    user_model = users_model.get_user(cid, ["user_id", "join_date", "email", "role", "email_verification"])
    # don't expose the email verification code to the template (replace with a bool...dynamic typing abuse)
    user_model["email_verification"] = not user_model["email_verification"]
    return user_model
