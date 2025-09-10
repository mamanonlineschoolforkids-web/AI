# 💬 FAQ Chatbot (Arabic & English)

## 🚀 Idea

This project is a simple **FAQ chatbot** that:

1. Loads predefined Q\&A pairs from a JSON file (`faq_data.json`).
2. Lets the user ask a question in **Arabic or English**.
3. Matches the input with existing questions using **fuzzy similarity**.
4. Returns the most relevant answers in the selected language.

---

## 🛠️ Requirements

* Python ≥ 3.9
* Install dependencies:

  ```bash
  pip install flask flask-ngrok pyngrok
  ```

---

## 📂 Project Structure

```
📦 FAQ-Chatbot
 ┣ 📜 faq_data.json     # FAQ dataset (Q&A in Arabic + English)
 ┣ 📜 faq_bot_smart_similarity.py    # Interactive chatbot
 ┗ 📜 README.md         # Project description
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

### 1️⃣ Interactive Mode

Run the chatbot in the terminal:

```bash
python faq_bot_smart_similarity.py
```

Sample conversation:

```
اكتب سؤالك (أو 'exit' للخروج): ما هو مأمن؟
اختر اللغة 'ar' للعربي أو 'en' للإنجليزي: ar

نتائج البحث:
سؤال: ما هو مأمن؟
إجابة: Ma’man هو منصة لإدارة المحتوى للأطفال والمراهقين.
```

---

## 🎯 Features

* Supports **Arabic & English**.
* Fuzzy search with **difflib SequenceMatcher**.
* Two modes: **interactive CLI** and **Flask REST API**.
* Easy to extend with new questions in `faq_data.json`.

---

## 📌 Notes

* Similarity is based on substring match + ratio (`SequenceMatcher`).
* Works best with well-structured and clean Q\&A data.
* If no match is found, a fallback message is returned.


