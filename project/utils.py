import hashlib
import random
import string

def placeholder_gen(things: list):
    return ', '.join("%s" for _ in things)

def comma_join(things: list):
    return ', '.join(things)

def random_string(length: int) -> str:
    return ''.join((random.choice(string.ascii_letters+string.digits)) for _ in range(length))


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