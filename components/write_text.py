import streamlit as st


def write_text(text):

    """
    Se encargará de escribir la seccion de texto pasada por parametro
    :param text: El texto que se imprimirá en la aplicación
    """

    html_result = "<p>"
    for word in text:
        if word[1] == "NOUN":
            html_result += " <strong>" + word[0] + "</strong>"
        elif word[1] == "PUNTC":
            html_result += word[0]
        else:
            html_result += " " + word[0]
    html_result += "</p>"
    st.markdown(html_result, unsafe_allow_html=True)
