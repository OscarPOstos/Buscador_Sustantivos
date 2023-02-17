import nltk
import spacy

nlp = spacy.load("es_core_news_sm")


def pos_tokenizer(text):
    doc = nlp(text)
    return [(token.text, token.pos_) for token in doc]
