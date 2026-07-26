from fastapi import FastAPI
from src.router import get_blog_router,post_blog_router,user_router,get_single_blogs,get_all_user_router,get_single_users
from src.database import engine,SQLModel
from src.models import blog_model,user_model

SQLModel.metadata.create_all(engine)


app=FastAPI()
@app.get("/")
def home():
    return "This is main appltion"

app.include_router(get_blog_router)
app.include_router(post_blog_router)
app.include_router(user_router)
app.include_router(get_single_blogs)
app.include_router(get_all_user_router)
app.include_router(get_single_users)
