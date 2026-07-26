from src.database.database_connection import get_session
from sqlmodel import select
from src.models.blog_model import Blogs

session=get_session()

def get_all_blog():
    get_blogs=session.exec(select(Blogs)).all()
    return get_blogs



def single_blog(id: int):
    with get_session() as session:
        statement = select(Blogs).where(Blogs.id == id)
        return session.exec(statement).first()