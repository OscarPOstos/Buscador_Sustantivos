import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import cess_esp
from nltk import tag

nltk.download('punkt')
nltk.download('cess_esp')
nltk.download('averaged_perceptron_tagger')


def pos_tokenizer(text):
    train_sents = cess_esp.tagged_sents()
    unigram_tagger = tag.UnigramTagger(train_sents)
    tokens = list(word_tokenize(text))
    return list(unigram_tagger.tag(tokens))
