import streamlit as st
from io import StringIO

st.title("Buscador de sustantivos")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    columns = st.columns(3)

    with columns[0]:
        title = st.checkbox("Titulo")
    with columns[1]:
        new = st.checkbox("Noticia")
    with columns[2]:
        summary = st.checkbox("Resumen")

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)