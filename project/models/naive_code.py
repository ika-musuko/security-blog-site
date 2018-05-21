import pymysql
from project import PYMYSQL_CONFIG

def verify_login_insecure(user_id: str, password: str):
    # even in the insecure code we don't want our actual database to be affected!
    if ";" in user_id or ";" in password:
        return None

    # connect to the database
    conn = pymysql.connect(**PYMYSQL_CONFIG)

    # space to store the result
    result = None

    try:
        with conn.cursor() as cursor:
            # see if the user_id and password match
            statement = 'SELECT user_id FROM insecure_users WHERE user_id="%s" AND password="%s";' % (user_id, password)
            cursor.execute(statement)

            result = cursor.fetchone()

    finally:
        # close the database connection
        conn.close()

        # return the result
        return result
