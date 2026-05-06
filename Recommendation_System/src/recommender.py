import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentRecommender:

    def __init__(self, path="data/content.csv"):
        self.df = pd.read_csv(path)

        self.df['title'] = self.df['title'].fillna("")
        self.df['description'] = self.df.get('description', "").fillna("")
        self.df['title_clean'] = self.df['title'].str.lower().str.strip()

        self.df['combined'] = self.df['title'] + " " + self.df['description']

        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf = self.vectorizer.fit_transform(self.df['combined'])

        self.similarity = cosine_similarity(self.tfidf)

    def recommend(self, title, k=5):

        title = title.lower().strip()

        matches = self.df[self.df['title_clean'].str.contains(title)]

        if len(matches) == 0:
            return []

        idx = matches.index[0]

        scores = list(enumerate(self.similarity[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        recs = []
        seen = set()
        input_title = self.df.iloc[idx]['title']

        for i in scores[1:]:
            if len(recs) >= k:
                break

            t = self.df.iloc[i[0]]['title']

            if t != input_title and t not in seen:
                recs.append(t)
                seen.add(t)

        return recs