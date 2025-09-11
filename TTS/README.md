# 🎤 Text-To-Speech (TTS) Project

Convert stories from **JSON files** into speech with support for **Arabic** and **English**.  
- Support for standard female voice.

---

## 📚 Features
- Read stories directly from JSON files (`stories_ar.json`, `stories_en.json`).
- Detect language automatically from the filename.
- Search stories by keyword in the title.
- Generate audio files (`.mp3`) for each story.
- Support for standard female voice.


---

## 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/<YourUsername>/Text-To-Speech.git
cd Text-To-Speech
````

Create a virtual environment (recommended):

```bash
python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Activate on Linux/Mac
source venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

---

## 📂 JSON File Structure

Example (`stories_en.json`):

```json
[
  {
    "id": 1,
    "title": "The School Adventure",
    "content": "Once upon a time, a group of students discovered a secret room..."
  }
]
```

Example (`stories_ar.json`):

```json
[
  {
    "id": 1,
    "title": "قصة نوح عليه السلام",
    "content": "أمر الله نبيه نوح عليه السلام أن يصنع سفينة..."
  }
]
```

---

## 🚀 Usage

Run the script:

```bash
python tts_stories.py
```

Search for a story by keyword:

```text
اكتب كلمة من عنوان القصة: adventure
```

Output:

```
✅ Found 1 story matching 'adventure':

1. The School Adventure (en)
```

Audio file generated in:

```
audio_stories/story_1_The_School_Adventure.mp3
```

---

## 📌 Requirements

* Python 3.9+
* [gTTS](https://pypi.org/project/gTTS/)
* IPython (for notebook playback)

Install manually if needed:

```bash
pip install gTTS ipython
```
