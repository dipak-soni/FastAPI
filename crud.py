from fastapi import FastAPI
from pydantic import BaseModel,Field
import json 

class Book(BaseModel):
    id:int=Field()
    name:str=Field()
    author:str=Field()
    year:int=Field()

app=FastAPI()
books=[]

@app.get('/')
def show_books():
    return books

@app.post('/create')
def add_book(request:Book):
    data=dict(request)
    books.append(data)
    return data


@app.get('/book/{id}')
def get_book(id:int):
    for i in books:
        if i['id']==id:
            return i
    return {'error':'Book not found'}

@app.put('/book/{id}')
def edit_book(id:int,request:Book):
    for i in books:
        if i['id']==id:
            i['name']=request.name
            i['author']=request.author
            i['year']=request.year
            return i
    return {'error':'Book not found'}


@app.delete('/book/{id}')
def delete_book(id:int):
    for i in books:
        if i['id']==id:
            books.remove(i)
            return {'message':'Book deleted'}
    return {'error':'Book not found'}