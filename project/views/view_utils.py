from project import app, POSTS_PER_PAGE

@app.context_processor
def inject_posts_per_page():
    return dict(POSTS_PER_PAGE=POSTS_PER_PAGE)