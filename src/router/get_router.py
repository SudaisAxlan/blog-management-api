from fastapi import APIRouter
from src.services import get_all_blogs,singles_blog



router=APIRouter(
    prefix="/blogs",
)

@router.get("/all_blogs")
def get_blogs():
    return get_all_blogs()


# @router.get("/single_blog")
# def get_single_blogs(id:int):
#     return single_blog(id=id)

@router.get("/single_blog/{id}")
def get_single_blogs(id: int):
    return singles_blog(id)