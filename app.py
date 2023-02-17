import streamlit as st
from io import StringIO

from string_transformer.personalized_string_class import PersonalizedStringClass
from pos_tokenizer.pos_tokenizer import pos_tokenizer

st.title("Buscador de sustantivos")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    columns = st.columns(3)

    with columns[0]:
        title = st.checkbox("Titulo", value=True)
    with columns[1]:
        new = st.checkbox("Noticia", value=True)
    with columns[2]:
        summary = st.checkbox("Resumen", value=True)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    with st.spinner('Buscando los sustantivos 😎'):
        test = pos_tokenizer(PersonalizedStringClass("Son 3 las muertes. conocidas en el día de hoy")
                             .text)
        html_result = "<p>"
        for word in test:
            if word[1].startswith("nc"):
                html_result += " <strong>" + word[0] + "</strong>"
            elif word[1] == "Fp":
                html_result += word[0]
            else:
                html_result += " " + word[0]
        html_result += "</p>"
        st.markdown(html_result, unsafe_allow_html=True)
