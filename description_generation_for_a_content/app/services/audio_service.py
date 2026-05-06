import os
import whisper
from moviepy import VideoFileClip
from app.services.text_service import generate_description

whisper_model = whisper.load_model("base")


def extract_audio(video_path, audio_path="temp/audio.wav"):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path, codec="pcm_s16le")
    return audio_path


def transcribe(path):
    return whisper_model.transcribe(path)["text"]


async def process_file(file):
    file_path = f"temp/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    ext = file.filename.split(".")[-1]

    if ext in ["mp4", "avi", "mov"]:
        audio = extract_audio(file_path)
        text = transcribe(audio)

    elif ext in ["mp3", "wav"]:
        text = transcribe(file_path)

    else:
        return {"error": "Unsupported file"}

    description = generate_description(text)

    return {"transcript": text, "description": description}