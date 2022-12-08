from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/")
def get_posts():
    return {"message": "Welcome to my api"}

@app.post("/")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"posts": "Returns all posts"}