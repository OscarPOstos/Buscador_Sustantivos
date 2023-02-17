import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def pos_tokenizer(text):
    return nltk.pos_tag(word_tokenize(text))
