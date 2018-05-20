from project import models


def query_posts(start, end):
    prepared_statement="SELECT post_id, title, date_created, preview, user_id FROM posts WHERE post_id < %s;"
    return models.get_sql(prepared_statement, values=[start], amount=start-end)

def get_post(post_id: int):
    prepared_statement="SELECT post_id, title, date_created, post_content, user_id FROM posts WHERE post_id = %s;"
    return models.get_sql(prepared_statement, values=[post_id], amount=1)

def get_total_posts():
    return models.get_sql_simple(statement="SELECT COUNT(post_id) FROM posts;", amount=1)["COUNT(post_id)"]

def add_post(user_id: str):
    # models.add_row("posts", {"title": "Hello Friends!", "date_created": datetime.datetime.now(), "preview": "Hello hello...", "user_id": "sherwyn", "post_content": "Hello hello hello"})
    pass