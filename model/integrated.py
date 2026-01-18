from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer, util
from model.preprocessor import categorize

model = SentenceTransformer("all-MiniLM-L6-v2")

category={"Gryffindor": "bold confident outspoken bravery nerve chivalry determination positive courage resilience moral outgoing good dependable",
          "Ravenclaw": "analytical logical knowledge witty creative original wise eccentric intuitive aloof pretentious judgemental",
          "Hufflepuff": "supportive loyal friendly fairness patience humility modesty tenacity just dedicated humble caring kind love amazing",
          "Slytherin": "persuasive sharp cunning leadership ambition prejudiced arrogant selfish sneaky pragmatism negative manipulative callousness ruthlessness cruel bad vindictive"}

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
    return max(scores, key=scores.get)  # type: ignore


def process(lines):
    messages = categorize(lines)
    res = {}
    for person in messages:
        freq={"Gryffindor":0, "Ravenclaw":0, "Hufflepuff":0, "Slytherin":0}
        for message in messages[person]:
            freq[classify_embedding(message)]+=1
        max_freq=max(freq.values())
        for h in freq:
            if freq[h]==max_freq:
                house=h
                break
        res[person]=house  # type: ignore
    return res