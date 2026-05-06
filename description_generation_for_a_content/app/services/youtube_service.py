from app.services.audio_service import transcribe
from app.services.text_service import generate_description
import yt_dlp
import os


def download_audio(url):
    os.makedirs("temp", exist_ok=True)

    output_template = "temp/youtube_audio"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template + '.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
        'socket_timeout': 300,
        'retries': 10,
        'fragment_retries': 10,
        'continuedl': True,
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return output_template + ".wav"


# 🔥 لازم تكون موجودة

def process_youtube(url):
    audio = download_audio(url)
    text = transcribe(audio)
    description = generate_description(text)

    return {
        "transcript": text,
        "description": description
    }