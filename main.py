# run the server 
# uvicorn main:app --reload
# main= module name
# app= FastAPI instance name
# http://localhost:8000/docs to enter the swagger UI api testing 
# http://localhost:8000/redoc to enter the redoc UI api testing

from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def index():
    return {"message":"Hello World"}

@app.get("/about")   # function name does not matter
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
