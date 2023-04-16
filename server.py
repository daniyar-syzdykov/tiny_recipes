from fastapi import FastAPI
from src.api.v1.views import main_router

app = FastAPI()
app.include_router(main_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
