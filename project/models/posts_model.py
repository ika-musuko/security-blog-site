from project import models


def query_posts(start, end):
    return models.get_sql_simple(statement="SELECT post_id, title, date_created, preview, user_id FROM posts WHERE post_id < " + str(end) + " ;", amount=start-end)


def get_total_posts():
    return models.get_sql_simple(statement="SELECT COUNT(post_id) FROM posts;", amount=1)["COUNT(post_id)"]