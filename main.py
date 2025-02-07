# run the server 
# uvicorn main:app --reload
# main= module name
# app= FastAPI instance name

from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def index():
    return {"message":"Hello World"}

@app.get("/about")   # function name does not matter
def index():
    return {"message":"About Page"}