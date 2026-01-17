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
    return max(scores, key=scores.get)

#Preprocessing 
messages = {}

def read_raw():
    lines = []
    with open("input.txt", 'r',  encoding='utf-8') as fin:
        lines = fin.readlines()
    return lines

def remove_timestamp(lines):
    modified = []
    for line in lines:
        modified.append(line.partition('-')[2])
    return modified

def categorize(lines):
    for line in lines:
        name, _, message = line.partition(':')
        message = message.strip()
        if name in messages:
            messages[name].append(message)
        else:
            messages[name] = [message]

categorize(remove_timestamp(read_raw()))

for key,val in messages.items():
    list_of_sentences=val
    sentence=" ".join(list_of_sentences)

    # Word Splitting
    tokens = word_tokenize(sentence.lower())

    # Stop Word Removal
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if w not in stop_words and w.isalnum()]
    characteristic=" ".join(filtered_tokens)

    print(key, classify_embedding(characteristic))

# classify_embedding("fear exactly figure")
