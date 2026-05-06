import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class FAQBot:
    def __init__(self, data_path=None):
        if data_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            data_path = os.path.join(base_dir, "data", "faq_data.json")

        with open(data_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        # 🔥 توحيد الداتا
        self.data = []

        for item in raw_data:
            if "question_ar" in item and "answer_ar" in item:
                self.data.append({
                    "question": item["question_ar"],
                    "answer": item["answer_ar"],
                    "lang": "ar"
                })

            if "question_en" in item and "answer_en" in item:
                self.data.append({
                    "question": item["question_en"],
                    "answer": item["answer_en"],
                    "lang": "en"
                })

        # حذف البيانات الفاضية
        self.data = [item for item in self.data if item["question"]]

        self.questions = [item["question"] for item in self.data]

        self.vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 4))
        self.X = self.vectorizer.fit_transform(self.questions)

    def find_similar(self, query, top_k=3, threshold=0.2):
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.X).flatten()

        top_indices = similarities.argsort()[-top_k:][::-1]

        results = []

        for idx in top_indices:
            if similarities[idx] < threshold:
                continue

            item = self.data[idx]
            results.append({
                "question": item["question"],
                "answer": item["answer"],
                "similarity": float(similarities[idx]),
                "lang": item["lang"]
            })

        return results

    def detect_language(self, text: str) -> str:
        return "ar" if any("\u0600" <= c <= "\u06FF" for c in text) else "en"