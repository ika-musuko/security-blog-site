import pymysql

from project import PYMYSQL_CONFIG


def db_connect():
    return pymysql.connect(**PYMYSQL_CONFIG)


def get_sql_simple(statement: str, amount: int=1):
    '''
    string concatenation get
    :param statement:
    :param amount:
    :return:
    '''
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


def get_sql(statement: str, values: list, amount: int=1):
    '''
    prepared sql get
    :param statement:
    :param values:
    :param amount:
    :return:
    '''
    conn = db_connect()
    result = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(statement, values)
            if amount > 1:
                result = cursor.fetchmany(size=amount)
            elif amount == 1:
                result = cursor.fetchone()
            else:
                result = cursor.fetchall()
    finally:
        conn.close()
        return result


def set_sql_simple(statement: str):
    '''
    string concatenation get, vulnerable to sql injections
    :param statement:
    :return:
    '''
    conn = db_connect()
    try:
        with conn.cursor as cursor:
            cursor.execute(statement)

        conn.commit()

    finally:
        conn.close()


def set_sql(statement: str, values: list):
    '''
    prepared sql get
    :param statement:
    :param values:
    :return:
    '''
    conn = db_connect()
    try:
        with conn.cursor as cursor:
            cursor.execute(statement, values)

        conn.commit()

    finally:
        conn.close()


def add_row(table: str, data: dict):
    keys = ', '.join(data.keys())
    vals = data.values()
    # generate the placeholders for the prepared SQL statement
    value_placeholders = ', '.join("%s" for _ in vals)

    # generate the SQL statement
    statement = "INSERT INTO %s (%s) VALUES(%s)" % (table, keys, value_placeholders)

    # set the sql (secure version)
    set_sql(statement, list(vals))
