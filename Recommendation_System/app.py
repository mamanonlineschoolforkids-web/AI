from fastapi import FastAPI, Query
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI(title="Content-Based Recommendation API")

# ================= LOAD DATA =================
df = pd.read_csv("E:\\faculty\\Ma'man\\Recommendation_System\\Recommendation_System\\data\\content.csv")

# clean titles
df['title'] = df['title'].fillna("")
df['title_clean'] = df['title'].str.strip().str.lower()

df['combined'] = df['title']

# ================= TF-IDF =================
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined'])

# similarity matrix
similarity = cosine_similarity(tfidf_matrix)


# ================= HELPER =================
def find_closest_title(title):
    """يدعم البحث الجزئي"""
    title = title.lower().strip()

    matches = df[df['title_clean'].str.contains(title)]

    if len(matches) == 0:
        return None

    return matches.iloc[0]['title_clean']


# ================= API =================

@app.get("/")
def home():
    return {"message": "API is running 🚀"}


@app.get("/recommend")
def recommend(title: str = Query(..., description="Enter course title"), k: int = 5):

    title_clean = find_closest_title(title)

    if title_clean is None:
        return {"error": "Title not found"}

    idx = df[df['title_clean'] == title_clean].index[0]

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommended = []
    seen_titles = set()
    input_title = df.iloc[idx]['title']

    for i in scores[1:]:
        if len(recommended) >= k:
            break

        rec_title = df.iloc[i[0]]['title']

        if rec_title != input_title and rec_title not in seen_titles:
            recommended.append(rec_title)
            seen_titles.add(rec_title)

    return {
        "input": input_title,
        "recommendations": recommended
    }