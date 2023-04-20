# main backend lAPI server file

from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title 1", "content": "content 1", "id": 1},
            {"title": "title 2", "content": "content 2", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


@app.get("/")
def root():
    return {"message": "Hello to my API"}


@app.get("/posts")
def get_posts():
    # return {"data": "This is your posts"}
    return {"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    print(post.dict())
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000000)
    my_posts.append(post_dict)
    # return {"data": f"new post"}
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_posts(id: int, response: Response):
    # print(type(id))
    post = find_post(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}

    # return {"post_detail": f"Here is post {id}"}

    return {"post_detail": post}
