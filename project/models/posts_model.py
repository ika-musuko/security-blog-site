from project import models, POSTS_PER_PAGE
import datetime

def query_posts(start, end, user_id: int=None):
    if user_id:
        prepared_statement="SELECT post_id, title, date_created, preview, user_id FROM posts WHERE user_id = %s ORDER BY date_created ASC;"
        values = [user_id]
    else:
        prepared_statement="SELECT post_id, title, date_created, preview, user_id FROM posts ORDER BY date_created DESC LIMIT %s, %s;"
        values = [end, start]
    print(prepared_statement, values)
    return models.get_sql(prepared_statement, values=values, amount=start-end)

def get_post(post_id: int):
    prepared_statement="SELECT post_id, title, date_created, post_content, user_id FROM posts WHERE post_id = %s;"
    return models.get_sql(prepared_statement, values=[post_id], amount=1)

def get_total_posts():
    return models.get_sql_simple(statement="SELECT COUNT(post_id) FROM posts;", amount=1)["COUNT(post_id)"]

def add_post(user_id: str, title: str, content: str):
    # models.add_row("posts", {"title": "Hello Friends!", "date_created": datetime.datetime.now(), "preview": "Hello hello...", "user_id": "sherwyn", "post_content": "Hello hello hello"})
    return models.add_row("posts", {
          "title" : title
        , "date_created" : datetime.datetime.now()
        , "preview" : content[:100]
        , "user_id" : user_id
        , "post_content" : content

    })

def edit_post(post_id: int, title: str, content: str):
    prepared_statement = "UPDATE posts SET title = %s, post_content = %s, preview = %s WHERE post_id = %s;"
    values = [title, content, content[:100], post_id]
    models.set_sql(prepared_statement, values)

def delete_post(post_id: int):
    prepared_statement = "DELETE FROM posts WHERE post_id = %s;"
    models.set_sql(prepared_statement, [post_id])