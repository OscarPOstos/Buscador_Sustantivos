import nltk
import spacy

nlp = spacy.load("es_core_news_sm")


def pos_tokenizer(text):
    """
    Aparte de tokenizar, extraera el tipo de palabra que es cada token
    :param text: El texto en el cual se realizará el preprocesamiento
    :return: Devuelve una lista donde cada elemento es otra lista de 2 elementos que serian
    la palabra y el tipo de palabra
    """
    doc = nlp(text)
    return [(token.text, token.pos_) for token in doc]
