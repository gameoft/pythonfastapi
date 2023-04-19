# main backend lAPI server file

from fastapi import FastAPI
from fastapi import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello to my API"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


@app.post("/create")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title {payload['title']} content {payload['content']}"}
