import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class FAQBot:
    def __init__(self, data_path='faq_data.json'):
        with open(data_path, 'r', encoding='utf-8') as f:
            self.faq_data = json.load(f)
        
        # Prepare questions for both languages
        self.questions = []
        self.answers = []
        for item in self.faq_data:
            self.questions.append(item['question_ar'])
            self.questions.append(item['question_en'])
            self.answers.append((item['answer_ar'], item['answer_en']))
        
        # Create TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(self.questions)
    
    @staticmethod
    def detect_language(text):
        for ch in text:
            if ('\u0600' <= ch <= '\u06FF' or
                '\u0750' <= ch <= '\u077F' or
                '\u08A0' <= ch <= '\u08FF' or
                '\uFB50' <= ch <= '\uFDFF' or
                '\uFE70' <= ch <= '\uFEFF'):
                return 'ar'
        return 'en'

    def find_similar(self, user_query, top_k=5, threshold=0.1):
        query_vector = self.vectorizer.transform([user_query])
        similarities = cosine_similarity(query_vector, self.question_vectors)[0]
        
        # Get top k results
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > threshold:
                q_idx = idx // 2  # Since we have ar and en for each
                lang = 'ar' if idx % 2 == 0 else 'en'
                results.append({
                    'question': self.questions[idx],
                    'answer': self.answers[q_idx][0] if lang == 'ar' else self.answers[q_idx][1],
                    'similarity': similarities[idx],
                    'lang': lang
                })
        
        return sorted(results, key=lambda x: x['similarity'], reverse=True)

# For backward compatibility
def search_similar_questions(user_input, top_k=5):
    bot = FAQBot()
    return [(r['similarity'], {'question_ar': r['question'] if r['lang'] == 'ar' else '', 
                               'question_en': r['question'] if r['lang'] == 'en' else '',
                               'answer_ar': r['answer'] if r['lang'] == 'ar' else '',
                               'answer_en': r['answer'] if r['lang'] == 'en' else ''}) for r in bot.find_similar(user_input, top_k)]