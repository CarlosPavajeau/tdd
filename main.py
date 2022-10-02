from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def root():
    return "Hello FastAPI"


@app.get("/is_prime/{number}")
async def is_prime(number: int):
    return True


@app.get("/fibonacci/{number}")
async def fibonacci(number: int):
    return 1
