from sqlmodel import select
from fastapi import HTTPException
from src.database.database_connection import get_session
from src.schama.blog_schama import BlogUpdate
from src.models.blog_model import Blogs

session=get_session()
def update_blog(id:int,user:BlogUpdate):
    update_blogs=session.exec(select(Blogs).where(Blogs.id==id)).first()
    if update_blogs is None:
            raise HTTPException(
                    status_code=404,
                    detail="User not found"
                )
    update_blogs.title=user.title
    update_blogs.author=user.author
    update_blogs.content=user.content

    session.add(update_blogs)
    session.commit()
    session.refresh(update_blogs)

    return {
            "status": "Success",
            "message": "Blog Updated Successfully",
            "blog": update_blogs
        }
