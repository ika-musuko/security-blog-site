class UserException(Exception):
    pass


class UserExistsException(UserException):
    pass


class InvalidVerification(UserException):
    pass


class EmailAlreadyVerified(UserException):
    pass