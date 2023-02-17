import nltk
from nltk.tokenize import word_tokenize


def pos_tokenizer(text):
    return nltk.pos_tag(word_tokenize(text))
