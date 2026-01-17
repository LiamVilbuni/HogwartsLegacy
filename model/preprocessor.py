import pandas as pd
from nltk import word_tokenize, sent_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

lemmatizer = WordNetLemmatizer()
STOP_WORDS = set(stopwords.words('english'))
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

        if (not len(_)):
            continue
        
        message = message.strip()
        if name in messages:
            messages[name].append(message)
        else:
            messages[name] = [message]


def get_wordnet_pos(tag):
    if tag.startswith('J'):  
        return 'a'
    elif tag.startswith('V'):  
        return 'v'
    elif tag.startswith('N'):  
        return 'n'
    elif tag.startswith('R'):  
        return 'r'
    else:
        return 'n'  


processed_data = {}

def tokenize_and_shi(messages, name):
    global processed_data
    tokens = set()
    for message in messages:
        sentences = sent_tokenize(message)
        for sentence in sentences:
            word_tokens = set()
            for word in sentence.split():
                word = word.replace("’", "'").lower()
                if (word not in STOP_WORDS) and word.isalnum():
                    word_tokens = word_tokens.union(set(word_tokenize(word)))
            word_tokens = pos_tag(word_tokens)
            for token in word_tokens:
                tokens = tokens.union({lemmatizer.lemmatize(token[0], get_wordnet_pos(token[1])),})
                
    processed_data[name] = tokens 


if __name__ == "__main__":
    categorize(remove_timestamp(read_raw()))
    print("---")
    for name in messages:
        tokenize_and_shi(messages[name], name)
    for name in processed_data:
        print(f"Tokens from {name}")
        print(processed_data[name])
