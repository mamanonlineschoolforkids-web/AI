# main.py
from preprocess import load_and_preprocess
from feature_engineering import build_tfidf_matrix, add_numeric_features
from hybrid import hybrid_recommend
import pandas as pd

def main():
    content_df, users, interactions = load_and_preprocess('content.csv','users.csv','interactions.csv')
    content_df = add_numeric_features(content_df)
    tfidf_vectorizer, tfidf_matrix = build_tfidf_matrix(content_df, max_features=2000)
    user_id = 1
    results = hybrid_recommend(user_id, users, interactions, content_df, tfidf_vectorizer, tfidf_matrix, top_n=5)
    print("Recommendations for user", user_id)
    print(results)

if __name__ == "__main__":
    main()
