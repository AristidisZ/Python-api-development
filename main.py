from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_post = [{"title": "title of post 1", "content": "content post 1", "id": 1}]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/posts")
def get_post():
    return {"data": my_post}

@app.post("/posts")
def create_post(post: Post):
    print(post)
    return {"data": post}
