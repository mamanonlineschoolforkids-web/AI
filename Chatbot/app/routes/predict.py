from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chatbot_service import get_response

router = APIRouter()

class QueryRequest(BaseModel):
    query: str
    lang: str | None = None


@router.post("/predict")
def predict(request: QueryRequest):
    response = get_response(request.query)  
    return {"results": response}