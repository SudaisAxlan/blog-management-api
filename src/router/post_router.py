from fastapi import APIRouter

from src.schama.blog_schama import BlogCreate,BlogUpdate
from src.services.post_blog import post_blog
from src.services import update_blog

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)


@router.post("/create_blog")
def create_new_blog(blog: BlogCreate):
    return post_blog(blog)



@router.put("/update_blog/{id}")
def update_existing_blog(id: int, blog: BlogUpdate):
    return update_blog(id, blog)