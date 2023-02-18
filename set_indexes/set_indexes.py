import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')


def set_indexes(text_file):
    """
    Saca las secciones de un texto y los convierte en un diccionario que contiene las secciones
    :param text_file: El texto contenido de un documento
    :return: Devuelve un diccionario con las secciones titulo, noticia y resumen
    """
    structure = {}
    key, texto = "", ""
    if len(text_file) == 6:
        for index in range(len(text_file)):
            if index % 2 == 0:
                key = text_file[index].strip()
            else:
                texto = " ".join(word_tokenize(text_file[index])).replace("\n", " ").strip()

            if key != "" and texto != "":
                structure[key.lower()] = texto
                key, texto = "", ""

    return structure
