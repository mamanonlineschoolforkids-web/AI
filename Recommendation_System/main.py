from fastapi import FastAPI
import numpy as np
import pickle
# import lightgbm as lgb
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# Load content data
content_df = pd.read_csv('content.csv')
content_df['combined'] = content_df['title'] + ' ' + content_df['description'] + ' ' + content_df['category']

# TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(content_df['combined'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get recommendations based on content similarity
def get_content_based_recommendations(content_id, topk=5):
    if content_id not in content_df['content_id'].values:
        return ["Invalid content ID"]
    
    idx = content_df[content_df['content_id'] == content_id].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:topk+1]  # Exclude self
    content_indices = [i[0] for i in sim_scores]
    return content_df['content_id'].iloc[content_indices].tolist()

# ===== Dummy recommend function (مبسطة) =====
def recommend(user_id, topk=5):
    # For now, recommend similar to a popular item, e.g., content_id 1
    return get_content_based_recommendations(1, topk)

# ===== Routes =====
@app.get("/")
def home():
    return {"message": "AI Recommendation API 🚀"}

@app.get("/recommend/{user_id}")
def get_recommendations(user_id: int):
    recs = recommend(user_id)
    return {
        "user_id": user_id,
        "recommendations": recs
    }