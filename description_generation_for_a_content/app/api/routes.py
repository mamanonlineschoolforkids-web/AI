from fastapi import APIRouter, UploadFile, File, Form
from app.services.audio_service import process_file
from app.services.youtube_service import process_youtube

router = APIRouter()


@router.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):
    return await process_file(file)


@router.post("/youtube")
def youtube_summary(url: str = Form(...)):
    return process_youtube(url)


@router.get("/")
def home():
    return {"message": "API Running 🚀"}