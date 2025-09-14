# description generation for a content

A Python project that converts any content (video, audio, text) into transcripts and generates safe, concise descriptions.

---

## Features

- Supports files:
  - Video: MP4, MOV, AVI  
  - Audio: MP3, WAV, M4A  
  - Text: TXT, PDF
- Converts audio to text automatically using **OpenAI Whisper**.
- Generates concise descriptions using **HuggingFace DistilBART**.
- Supports downloading audio directly from **YouTube**.
- Splits long texts to avoid model input length issues.
- Cleans text from unwanted symbols and extra spaces.

---

## Requirements

```bash
pip install moviepy openai-whisper transformers torch PyPDF2 yt-dlp
pip install PyPDF2
pip install yt-dlp openai-whisper transformers torch
````

---

## Usage

### 1️⃣ Local Video/Audio/Text Content

```python
from your_module import process_content

file_path = "Lecture 1.pdf"  # Example: video, audio, text
transcript, description = process_content(file_path)

print("Transcript:\n", transcript)
print("Description:\n", description)
```

### 2️⃣ Download Audio from YouTube

```python
from your_module import download_youtube_audio, transcribe_audio, generate_description

youtube_url = "https://www.youtube.com/shorts/9IZOLy-Hz4c"
audio_file = download_youtube_audio(youtube_url)

transcript = transcribe_audio(audio_file)
description = generate_description(transcript)

print("Transcript:\n", transcript)
print("Description:\n", description)
```

---

## Notes

* For very short texts, the original text is used as the description.
* The code supports both Arabic and English automatically.
* You can change the Whisper model to `"small"` or `"medium"` for faster processing or higher accuracy.


