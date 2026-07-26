from src.schama.blog_schama import BlogCreate
from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def home():
    return "this is the hoem screen in test data"

@app.post("/create_blog")
def create_blogs(user:BlogCreate):
    new_user={
        "title":user.title,
        "author":user.author,
        "content":user.content,
        "user_id":user.user_id
    }
    return{
        "status":"Sucessfully",
        "message":"Blogs Created Sucessfully",
        "user":new_user

    }