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
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i = i + 6
    return True


@app.get("/fibonacci/{number}")
async def fibonacci(number: int):
    return 1
