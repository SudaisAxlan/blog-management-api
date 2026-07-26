from fastapi import APIRouter

from src.schama.blog_schama import BlogCreate
from src.services.post_blog import post_blog

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)


@router.post("/create_blog")
def create_new_blog(blog: BlogCreate):
    return post_blog(blog)