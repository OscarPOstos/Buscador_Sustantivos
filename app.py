import streamlit as st
from io import StringIO
from PIL import Image

from pos_tokenizer.pos_tokenizer import pos_tokenizer
from style.style import set_style
from components.write_text import write_text
from set_indexes.set_indexes import set_indexes

"""
Aqui se irá construyendo la interfaz de la aplicación y añadiendo sus funcionalidades
"""

set_style()

st.title("Buscador de sustantivos")

uploaded_file = st.file_uploader("Elige un archivo", type="txt")
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
    try:
        with st.spinner('Buscando los sustantivos 😎'):
            title_text = pos_tokenizer(indexes["titulo"])
            news_text = pos_tokenizer(indexes["noticia"])
            summary_text = pos_tokenizer(indexes["resumen"])
        if title:
            st.write("Titulo")
            write_text(title_text)
        if news:
            st.write("Noticia")
            write_text(news_text)
        if summary:
            st.write("Resumen")
            write_text(summary_text)
    except KeyError:
        st.title("Lo sentimos pero el archivo no cumple la estructura permitida :(")
        st.write("Debe tener una estructura parecida a esta")
        image = Image.open('images/estructura.png')
        st.image(image)
