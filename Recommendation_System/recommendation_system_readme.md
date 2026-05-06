# 📌 Recommendation System Project

## 🚀 Project Overview

This project implements a **Content-Based Recommendation System API** for educational courses using **FastAPI**.

It recommends similar courses based on **text similarity (TF-IDF + Cosine Similarity)** using course titles.

The system also supports **partial title search** to handle user input flexibility.

---

## ✨ Features

* 🔍 Content-based recommendation using course titles
* 🧠 TF-IDF + Cosine Similarity model
* 🔎 Partial title matching (fuzzy search)
* ⚡ FastAPI REST API
* 🎯 Top-k recommendations
* 🧾 Clean structured JSON response
* 🖥 Streamlit UI support (frontend)

---

## 📂 Dataset

The system uses a dataset:

* `content.csv`

  * `title`: Course title
  * (optional other metadata)

---

## 🧹 Data Preprocessing

* Missing titles filled with empty strings
* Titles cleaned (lowercase + strip)
* Combined text features created from title
* TF-IDF vectorization applied to text
* Cosine similarity computed between all courses

---

## 🤖 Model Architecture

### 📌 1. TF-IDF Vectorizer

Converts course titles into numerical vectors:

\text{TF-IDF}(t,d) = \text{TF}(t,d) \times \text{IDF}(t)

* Captures importance of words in titles
* Removes common words (stopwords)

---

### 📌 2. Cosine Similarity

\text{similarity}(A,B)=\frac{A \cdot B}{|A|,|B|}

* Measures similarity between course vectors
* Used to rank recommendations

---

## 🔥 API Endpoints

### 🏠 Home

```http
GET /
```

Response:

```json
{
  "message": "API is running 🚀"
}
```

---

### 🎯 Get Recommendations

```http
GET /recommend?title=python&k=5
```

### Parameters:

* `title` → course title (or partial title)
* `k` → number of recommendations

---

### 📤 Response Example:

```json
{
  "input": "Python for Beginners",
  "recommendations": [
    "Natural Language Processing with Python",
    "Computer Vision Basics",
    "Mobile App Development with Flutter",
    "Power BI for Data Analysis",
    "Artificial Intelligence Fundamentals"
  ]
}
```

---

## 🔎 Smart Search Feature

The system supports **partial matching**:

✔ Input:

```
"Data"
```

✔ Output:

* Data Science Course
* Data Analysis with Python
* Data Engineering Basics

---

## 🖥 Streamlit Frontend

A simple UI built with Streamlit:

### Features:

* Enter course title
* Choose number of recommendations
* Display ranked results

### API call:

```python
requests.get("http://127.0.0.1:8000/recommend", params={
    "title": title,
    "k": k
})
```

---

## ⚙️ Tech Stack

* FastAPI
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity
* Requests (API calls)

---

## 🚀 How to Run Project

### 1️⃣ Run FastAPI Backend

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 📊 Evaluation (Optional Extension)

Future improvements can include:

* Precision@k
* Recall@k
* NDCG@k
* User feedback loop

---

## 📦 Installation

```bash
pip install fastapi uvicorn pandas scikit-learn requests
```

---

## 💡 Future Improvements

* Add collaborative filtering (LightFM)
* Add ranking model (LightGBM)
* Deploy on Railway / Render
* Add user personalization
* Add vector database (FAISS)

---

## 👩‍💻 Author

AI Recommendation System Project 🚀

