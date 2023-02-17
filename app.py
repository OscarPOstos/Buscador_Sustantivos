import streamlit as st
from io import StringIO

from pos_tokenizer.pos_tokenizer import pos_tokenizer
from style.style import set_style
from components.write_text import write_text
from set_indexes.set_indexes import set_indexes

set_style()

st.title("Buscador de sustantivos")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    columns = st.columns(3)

    with columns[0]:
        title = st.checkbox("Titulo", value=True)
    with columns[1]:
        news = st.checkbox("Noticia", value=True)
    with columns[2]:
        summary = st.checkbox("Resumen", value=True)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    string_data = stringio.read()
    indexes = set_indexes(string_data.split("\r\n\r"))
    with st.spinner('Buscando los sustantivos 😎'):
        title_text = pos_tokenizer(indexes["titulo"])
        news_text = pos_tokenizer(indexes["noticia"])
        summary_text = pos_tokenizer(indexes["resumen"])


    with st.spinner('Buscando los sustantivos 😎'):
        if title:
            write_text(title_text)
        if news:
            write_text(news_text)
        if summary:
            write_text(summary_text)
