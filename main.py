from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to my api"}

@app.get("/posts")
async def posts():
    return {"posts": "Returns all posts"}