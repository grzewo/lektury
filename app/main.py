from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/hello")
async def read_hello():
    return {"message": "Hello Grzegorz"}


@app.get("/number")
async def read_number():
    return {"number": 24}
