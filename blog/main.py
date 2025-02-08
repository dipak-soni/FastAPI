from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field
from uuid import UUID
from .database import engine,sessionmaker
from sqlalchemy.orm import Session  
import models

app=FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionmaker()
    try:
        yield db
    finally:
        db.close()

class Book(BaseModel):
    id: UUID = Field(min_length=1,max_length=100)
    title: str=Field(min_length=5)
    author: str=Field(min_length=5)
    year: int=Field(min_value=1900,max_value=2021)
    rating: int=Field(min_value=1,max_value=5) 

books = []

@app.get('/books')
def get_books():
    return books

