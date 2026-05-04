# 💬 FAQ Chatbot (Arabic & English)

## 🚀 Idea

This project is a **FAQ chatbot** that:

1. Loads predefined Q&A pairs from a JSON file (`faq_data.json`).
2. Lets the user ask a question in **Arabic or English**.
3. Matches the input with existing questions using **TF-IDF similarity** (via scikit-learn).
4. Returns the most relevant answers in the selected language.
5. Provides both **interactive notebook mode** and **Flask REST API** for web integration.

---

## 🛠️ Requirements

* Python ≥ 3.9
* Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

---

## 📂 Project Structure

```
📦 FAQ-Chatbot
 ┣ 📜 faq_data.json          # FAQ dataset (Q&A in Arabic + English)
 ┣ 📜 model.py               # FAQBot class with TF-IDF similarity
 ┣ 📜 app.py                 # Flask REST API server
 ┣ 📜 faq_bot_smart_similarity.ipynb  # Interactive Jupyter notebook
 ┣ 📜 requirements.txt       # Python dependencies
 ┗ 📜 README.md              # Project description
```

---

## 📌 FAQ JSON Format

Your `faq_data.json` must follow this structure:

```json
[
  {
    "question_ar": "ما هو مأمن؟",
    "answer_ar": "Ma’man هو منصة لإدارة المحتوى للأطفال والمراهقين.",
    "question_en": "What is Ma'man?",
    "answer_en": "Ma’man is a content management platform for kids and teens."
  },
  {
    "question_ar": "كيف يمكنني التسجيل؟",
    "answer_ar": "يمكنك التسجيل عبر الموقع الإلكتروني.",
    "question_en": "How can I register?",
    "answer_en": "You can register through the website."
  }
]
```

---

## ⚙️ How It Works

### 1️⃣ Interactive Notebook Mode

Open `faq_bot_smart_similarity.ipynb` in Jupyter and run the cells:

1. Install packages (if needed).
2. Import and initialize the bot.
3. Test with a sample query.
4. Run the interactive loop to ask questions.

Sample conversation:

```
اكتب سؤالك (أو 'exit' للخروج): ما هو مأمن؟
اختر اللغة 'ar' للعربي أو 'en' للإنجليزي (أو اضغط Enter للكشف التلقائي): ar

نتائج البحث:
سؤال: ما هو مأمن؟
إجابة: Ma’man هو منصة لإدارة المحتوى للأطفال والمراهقين.
تشابه: 1.00
```

### 2️⃣ Flask REST API Mode

Run the API server:

```bash
python app.py
```

The server will start and provide a public URL via ngrok.

Send POST requests to `/chat`:

```json
{
  "question": "ما هو مأمن؟",
  "lang": "ar"
}
```

Response:

```json
{
  "results": [
    {
      "question": "ما هو مأمن؟",
      "answer": "Ma’man هو منصة لإدارة المحتوى للأطفال والمراهقين.",
      "similarity": 1.0
    }
  ]
}
```

---

## 🎯 Features

* Supports **Arabic & English** with automatic language detection.
* Advanced similarity search using **TF-IDF and cosine similarity**.
* Two modes: **interactive notebook** and **REST API**.
* Easy to extend with new questions in `faq_data.json`.
* Fallback messages when no suitable answer is found.

---

## 📌 Notes

* Similarity is calculated using TF-IDF vectorization and cosine similarity.
* Works best with well-structured Q&A data.
* If no match is found above the threshold, a fallback message is returned.
* The API uses ngrok for public access (requires ngrok auth token if not set).


