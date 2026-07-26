from src.schama.blog_schama import BlogCreate
from src.models.blog_model import Blogs
from src.database.database_connection import get_session


def post_blog(blog: BlogCreate):

    new_blog = Blogs(
        title=blog.title,
        author=blog.author,
        content=blog.content,
        user_id=blog.user_id
    )
    session=get_session()
    # with get_session() as session:
    session.add(new_blog)
    session.commit()
    session.refresh(new_blog)
    

    return {
        "status": "Successfully",
        "message": "Blog Added Successfully",
        "blog": new_blog
    }