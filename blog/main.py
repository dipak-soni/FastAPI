from fastapi import FastAPI

app = FastAPI()

@app.post('/blog')
def create_blog(title,body):
    return {"data":"Blog is created"}
