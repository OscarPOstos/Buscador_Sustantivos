import nltk
from nltk.tokenize import word_tokenize
import streamlit as st

nltk.download('punkt')


def set_indexes(text_file):
    structure = {}
    key, texto = "", ""
    st.write(len(text_file))
    if len(text_file) == 6:
        for index in range(len(text_file)):
            if index % 2 == 0:
                key = text_file[index]
            else:
                texto = ",".join(word_tokenize(text_file[index])).replace(",", " ").replace("\n", " ")

            if key != "" and texto != "":
                structure[key.lower()] = texto
                key, texto = "", ""

    return structure
