import hashlib
import random
import string
import re

def sql_placeholder_gen(things: list):
    return ', '.join("%s" for _ in things)

def comma_join(things: list):
    return ', '.join(things)

def random_string(length: int) -> str:
    return ''.join((random.choice(string.ascii_letters+string.digits)) for _ in range(length))

def check_valid_email_address(email: str):
     return re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

def hash_password(password, salt):
    '''
    hash a password with a salt
    :param password:
    :param salt:
    :return:
    '''
    hash_object = hashlib.sha224(''.join((password, salt)).encode())
    hash_code = hash_object.hexdigest()
    return hash_code.encode()

def censor_email(email: str):
    email_name, email_address = email.split('@')
    return "%s%s@%s" % (email_name[:2], ''.join(('*' for _ in range(len(email_name)-2))), email_address)


def check_valid_password(password: str) -> bool:

    # check each condition individually to prevent linearization attack
    password_conditions = [
          len(password) > 7
        , not (not any(c.isupper() for c in password)) # make sure that every character is checked and no short circuit happens
        , not (not any(c.islower() for c in password))
        , not (not any(c.isnumeric() for c in password))
        , not (not any(c in "!@#$%^&*" for c in password))
    ]
    return all(password_conditions) # if all conditions are true