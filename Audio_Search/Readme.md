# 📖 Interactive Story Search with Whisper

## 🚀 Idea

This project allows you to:

1. Record your voice 🎙️ (Arabic or English).
2. Convert speech to text using **Whisper**.
3. Auto-detect the language (Arabic / English).
4. Search for a matching story in JSON files (Arabic + English).
5. Display the selected story 📖.
6. Listen to the story using **Text-to-Speech (gTTS)** 🔊.

---

## 🛠️ Requirements

* Google Colab (or Python with Jupyter Notebook).
* Python ≥ 3.9
* Install dependencies:

  ```bash
  pip install torchaudio pydub rapidfuzz gTTS langdetect openai-whisper
  ```

---

## 📂 Project Structure

```
📦 Project
 ┣ 📜 stories_ar.json   # Stories in Arabic
 ┣ 📜 stories_en.json   # Stories in English
 ┣ 📜 Audio_Search(ar,en).ipynb    # Main code
 ┗ 📜 README.md         # Project description
```

---

## ⚙️ How It Works

### 1️⃣ Install dependencies

```python
!pip install -q torchaudio pydub rapidfuzz gTTS langdetect openai-whisper
```

### 2️⃣ Load Whisper model

```python
import whisper
model = whisper.load_model("small")
```

### 3️⃣ Upload story files

```python
from google.colab import files
uploaded_ar = files.upload()  # stories_ar.json
uploaded_en = files.upload()  # stories_en.json
```

### 4️⃣ Record audio

A recording button appears in Colab:

* Click 🎙️ **“Record”**
* Speak for 5 seconds
* Audio will be converted into text

### 5️⃣ Search & Display

* Similarity is calculated with **RapidFuzz**
* Matching stories will appear as clickable buttons

### 6️⃣ Listen to the story

* Story is displayed as text
* An MP3 is generated so you can listen to it

---

## 🎯 Features

* Supports **two languages (Arabic/English)**.
* Smart fuzzy search in titles and text.
* Speech-to-Text with **Whisper**.
* Text-to-Speech with **gTTS**.
* Simple interactive interface in Colab.

---

## 📌 Notes

* Whisper works best with GPU (use **Google Colab GPU** for faster results).
* Stories must follow the **JSON format**:

  ```json
  [
    {"title": "Lion Story", "content": "Once upon a time..."},
    {"title": "قصة الأسد", "text": "كان يا مكان..."}
  ]
  ```

