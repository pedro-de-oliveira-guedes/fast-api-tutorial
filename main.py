from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"name": "John Doe", "Message": "Hello World"}
