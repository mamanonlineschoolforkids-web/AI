from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import os
import whisper
import yt_dlp
import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from moviepy import VideoFileClip

app = FastAPI(title="Media Transcription & Summarization API")

# ---------- Models ----------

# Whisper model (خفيف عشان التشغيل ما يهنجش)
whisper_model = whisper.load_model("small")

# FLAN-T5 correct setup
model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

summarizer = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer
)

# ---------- Utils ----------

def extract_audio_from_video(video_path, audio_path="temp_audio.wav"):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    return audio_path


def transcribe_audio(file_path):
    result = whisper_model.transcribe(file_path)
    return result["text"]


def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^ء-يA-Za-z0-9 .,!?]', '', text)
    return text.strip()


def split_text(text, max_words=200):
    words = text.split()
    return [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)]


def generate_description(text):
    text = clean_text(text)

    if len(text.split()) < 50:
        return text

    chunks = split_text(text)
    summaries = []

    for chunk in chunks:
        try:
            prompt = f"summarize: {chunk}"

            output = summarizer(
                prompt,
                max_length=60,
                min_length=20,
                do_sample=False
            )

            summaries.append(output[0]["generated_text"])

        except Exception as e:
            print("Error in chunk:", e)
            continue

    return " ".join(summaries)


def download_youtube_audio(url):
    output_file = "youtube_audio"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_file,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return output_file + ".mp3"


# ---------- API Routes ----------

@app.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    ext = file.filename.split(".")[-1].lower()

    if ext in ["mp4", "avi", "mov"]:
        audio_path = extract_audio_from_video(file_path)
        text = transcribe_audio(audio_path)

    elif ext in ["mp3", "wav", "m4a"]:
        text = transcribe_audio(file_path)

    elif ext == "txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    else:
        return JSONResponse({"error": "Unsupported file type"})

    description = generate_description(text)

    return {
        "transcript": text,
        "description": description
    }


@app.post("/youtube")
def youtube_summary(url: str = Form(...)):
    audio_file = download_youtube_audio(url)
    text = transcribe_audio(audio_file)
    text = clean_text(text)
    description = generate_description(text)

    return {
        "transcript": text,
        "description": description
    }


@app.get("/")
def home():
    return {"message": "API is running 🚀"}