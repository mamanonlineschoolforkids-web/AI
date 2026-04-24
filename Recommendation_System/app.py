from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# 1. تحميل الداتا
df = pd.read_csv("content.csv")
df['combined'] = df['title']
df['title_clean'] = df['title'].str.strip().str.lower()

# 2. تحويل النصوص لفكتورز
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])

# 3. similarity matrix
similarity = cosine_similarity(tfidf_matrix)

# 4. API الرئيسية
@app.get("/recommend/{title}")
def recommend(title: str):

    title_clean = title.strip().lower()
    if title_clean not in df['title_clean'].values:
        return {"error": "Title not found"}

    idx = df[df['title_clean'] == title_clean].index[0]

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # top 5 recommendations, skip same title and duplicates
    recommended = []
    seen_titles = set()
    input_title = df.iloc[idx]['title']
    for i in scores[1:]:  # start from 1 to skip self
        if len(recommended) >= 5:
            break
        rec_title = df.iloc[i[0]]['title']
        if rec_title != input_title and rec_title not in seen_titles:
            recommended.append(rec_title)
            seen_titles.add(rec_title)

    return {
        "input": input_title,
        "recommendations": recommended
    }