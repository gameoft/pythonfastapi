# main backend lAPI server file

from typing import Optional
from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello to my API"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


@app.post("/create")
def create_posts(new_post: Post):
    print(new_post)
    print(new_post.title)
    return {"data": f"new post"}
