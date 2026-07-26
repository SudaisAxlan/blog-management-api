from pydantic import BaseModel

class BlogCreate(BaseModel):
    title: str
    author: str
    content: str
    user_id: int


class BlogUpdate(BaseModel):
    title: str
    author: str
    content: str