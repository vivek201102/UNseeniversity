from fastapi import FastAPI

app = FastAPI(title="UNseeniversity")

@app.get("/")
def read_root():
    return {"message": "Hello World"}