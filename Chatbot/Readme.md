# 💬 FAQ Chatbot (Arabic & English)

## 🚀 Overview

This project is an **intelligent multilingual FAQ Chatbot** that:

- Loads Q&A data from a JSON file (`faq_data.json`)
- Supports **Arabic & English**
- Automatically detects the language of the user query
- Uses **TF-IDF + Cosine Similarity** to find the most relevant answer
- Provides both:
  - 🧪 Interactive testing (Notebook)
  - 🌐 REST API using FastAPI

---

## 🧠 How It Works

1. User enters a question
2. System automatically detects language (Arabic / English)
3. Text is vectorized using **TF-IDF (character n-grams)**
4. Similarity is calculated using **Cosine Similarity**
5. Best matching answer is returned

---

## 🛠️ Tech Stack

- Python 3.9+
- FastAPI
- scikit-learn
- NumPy
- JSON dataset

---

## 📂 Project Structure

```

📦 FAQ-Chatbot
┣ 📁 app/
┃ ┣ 📄 main.py
┃ ┣ 📁 routes/
┃ ┃ ┗ 📄 predict.py
┃ ┣ 📁 services/
┃ ┃ ┗ 📄 chatbot_service.py
┃ ┣ 📁 utils/
┃ ┃ ┗ 📄 language.py
┃ ┗ 📄 config.py
┃
┣ 📁 model/
┃ ┣ 📄 faq_bot.py
┃ ┗ 📁 data/
┃ ┃ ┗ 📄 faq_data.json
┃
┣ 📓 notebooks/
┃ ┗ 📄 testing.ipynb
┃
┣ 📄 requirements.txt
┣ 📄 run.py
┗ 📄 README.md

````

---

## 📌 Dataset Format (JSON)

The dataset must follow this structure:

```json
[
  {
    "question_ar": "ما هو مأمن؟",
    "answer_ar": "Ma’man هو منصة لإدارة المحتوى للأطفال والمراهقين.",
    "question_en": "What is Ma'man?",
    "answer_en": "Ma’man is a content management platform for kids and teens."
  }
]
````

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Project

### ▶️ 1. Run FastAPI Server

```bash
python run.py
```

or

```bash
uvicorn app.main:app --reload
```

---

### 🌐 API Documentation

After running the server, open:

```
http://127.0.0.1:8000/docs#/
```

---

## 📡 API Usage

### 📥 Request

```http
POST /predict
```

```json
{
  "query": "ما هو مأمن؟"
}
```

---

### 📤 Response

```json
{
  "results": [
    {
      "question": "ما هو مأمن؟",
      "answer": "Ma’man هو منصة لإدارة المحتوى للأطفال والمراهقين.",
      "similarity": 0.92,
      "lang": "ar"
    }
  ]
}
```

---

## 🧪 Interactive Notebook

You can test the model using:

```
notebooks\faq_bot_smart_similarity.ipynb
```

Features:

* Manual testing
* Language detection demo
* Interactive chatbot mode

---

## 🎯 Features

* 🌍 Multilingual (Arabic + English)
* 🧠 Automatic language detection
* 🔍 TF-IDF similarity search
* ⚡ Fast API using FastAPI
* 📊 Clean and scalable architecture
* 🧪 Notebook-based testing

---

## 🔮 Future Improvements

* Replace TF-IDF with BERT embeddings
* Add semantic search (AI-powered understanding)
* Add database support (MongoDB / PostgreSQL)

---

## 👨‍💻 Author

Built as an AI/NLP learning project for FAQ retrieval systems.

```
