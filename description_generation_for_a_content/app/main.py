from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Media AI API")

app.include_router(router)