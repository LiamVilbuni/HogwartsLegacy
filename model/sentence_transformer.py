from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

category={"Gryffindor": "bold confident outspoken",
          "Ravenclaw": "analytical logical knowledge",
          "Hufflepuff": "supportive loyal friendly",
          "Slytherin": "strategic persuasive sharp"}

cat_embeddings = {
    cat: model.encode(text)
    for cat, text in category.items()
}

def classify_embedding(text):
    emb = model.encode(text)
    scores = {
        cat: util.cos_sim(emb, cat_emb).item()
        for cat, cat_emb in cat_embeddings.items()
    }
    return max(scores, key=scores.get),scores

# classify_embedding("fear exactly figure")
