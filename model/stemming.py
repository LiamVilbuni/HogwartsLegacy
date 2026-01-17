from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

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
    text=sentence

    # Word Splitting
    tokens = word_tokenize(text.lower())

    # Stop Word Removal
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if w not in stop_words and w.isalnum()]

    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(w) for w in filtered_tokens]
    print(f"{key}'s Stemmed Tokens: {stemmed_tokens}")
        

