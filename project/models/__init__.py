import pymysql

from project import PYMYSQL_CONFIG

from functools import wraps


def db_connect():
    return pymysql.connect(**PYMYSQL_CONFIG)


def get_sql(statement: str, amount: int=1):
    conn = db_connect()
    result = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(statement)
            if amount > 1:
                result = cursor.fetchmany(size=amount)
            elif amount == 1:
                result = cursor.fetchone()
            else:
                result = cursor.fetchall()
    finally:
        conn.close()
        return result


def set_sql(statement: str, amount: int=1):
    conn = db_connect()
    try:
        with conn.cursor as cursor:
            cursor.execute(statement)

        conn.commit()

    finally:
        conn.close()


def query_posts(start, end):
    return get_sql(statement="SELECT `post_id`, `title`, `date_created`, `preview`, `user_id` FROM `posts` WHERE `post_id` < " + end + " ;", amount=start-end)

def get_total_posts():
    return get_sql(statement="SELECT COUNT(`post_id`) FROM `posts`;", amount=1)



