from sqlmodel import SQLModel, Field
from typing import Optional

class Blogs(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author:str
    content: str

    user_id: int = Field(foreign_key="users.id")