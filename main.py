from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def root():
  return "Hello FastAPI"
