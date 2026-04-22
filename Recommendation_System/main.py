from fastapi import FastAPI
import numpy as np
import pickle
import lightgbm as lgb

app = FastAPI()

# ===== Load Models =====
with open("model/user2index.pkl", "rb") as f:
    user2index = pickle.load(f)

with open("model/item2index.pkl", "rb") as f:
    item2index = pickle.load(f)

with open("model/index2item.pkl", "rb") as f:
    index2item = pickle.load(f)

user_embeddings = np.load("model/user_embeddings.npy")
item_embeddings = np.load("model/item_embeddings.npy")

with open("model/lightfm_model.pkl", "rb") as f:
    lfm_model = pickle.load(f)

ranker = lgb.Booster(model_file="model/ranker_model.txt")

# ===== Dummy recommend function (مبسطة) =====
def recommend(user_id, topk=5):
    if user_id not in user2index:
        return ["No recommendations"]

    uidx = user2index[user_id]
    scores = np.dot(item_embeddings, user_embeddings[uidx])
    top_items = np.argsort(-scores)[:topk]

    return [int(index2item[i]) for i in top_items]

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