from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def get_posts():
    return {"message": "Welcome to my api"}

@app.post("/")
def create_post(post: Post):
    print()
    return {"posts": post}