# from src.schama.blog_schama import BlogCreate
from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def home():
    return "this is the hoem screen in test data"
