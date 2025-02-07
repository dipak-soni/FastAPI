# run the server 
# uvicorn main:app --reload
# main= module name
# app= FastAPI instance name
# http://localhost:8000/docs to enter the swagger UI api testing 
# http://localhost:8000/redoc to enter the redoc UI api testing

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app=FastAPI()

@app.get("/")
def index():
    return {"message":"Hello World"}

@app.get("/about")   # similar function name does not matter
def index():
    return {"message":"About Page"}

# dynamic taking data from path
@app.get("/blog/{id}")
def index(id):
    # fetch blog with id ==
    return {"data":id}


@app.get("/blog/{id}/comments")
def index(id:int):
    # fetch comments with id
    return {"comments":"This is a comment section"}

@app.get("/blogs")
def index(limit):
    # https://localhost:8000/blogs?limit=10
    # 10 blogs would be shown 
    # in this case query parameter is necessary
    return {"data":f"{limit} created "}


@app.get("/blogs")
def index(limit=10):
    # https://localhost:8000/blogs
    # 10 blogs would be shown 
    # in this case query parameter is not necessary
    return {"data":f"{limit} created "}



# Post request 
@app.post("/create_blog")
def create_blog():
    return {"data":"Blog is created"}

# How to create request body
class Blog(BaseModel):
    username:int
    comment:str
    published_at:bool

@app.post("/create_blog_with_body")
def create_blog_with_body(request:Blog):
    return {"data":f"Blog is created with {request.username}"}


# if __name__=="__main__":
#     uvicorn.run(app,host="localhost",port=8000)


# crud operations 
# go to blog folder