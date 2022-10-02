from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def root():
    return "Hello FastAPI"


@app.get("/is_prime/{number}")
async def is_prime(number: int):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    return True


@app.get("/fibonacci/{number}")
async def fibonacci(number: int):
    return 1
