import ntlk
from nltk.tokenize import word_tokenize


def pos_tokenizer(text):
    return ntlk.pos_tag(word_tokenize(text))
