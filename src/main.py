# from sqlmodel import SQLModel
from database import engine,SQLModel
from models import blog_model,user_model

SQLModel.metadata.create_all(engine)
print("Datasbe created sucessfully ")

