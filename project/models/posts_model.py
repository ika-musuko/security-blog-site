from project.models import get_sql


def query_posts(start, end):
    return get_sql(statement="SELECT `post_id`, `title`, `date_created`, `preview`, `user_id` FROM `posts` WHERE `post_id` < " + end + " ;", amount=start-end)


def get_total_posts():
    return get_sql(statement="SELECT COUNT(`post_id`) FROM `posts`;", amount=1)