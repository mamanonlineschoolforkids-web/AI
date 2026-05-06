from fastapi import FastAPI
from app.routes.predict import router

def create_app():
    app = FastAPI(title="FAQ Chatbot API")

    app.include_router(router)

    return app


app = create_app()