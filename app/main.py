# main backend lAPI server file

from typing import Optional
from fastapi import FastAPI, status, HTTPException
from fastapi import Response
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


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


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


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    my_posts.pop(index)
    # return {"message": "post deleted"}
    return Response(None, status.HTTP_204_NO_CONTENT)


# @app.put("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    print(post)
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict
    return {"data": post_dict}
