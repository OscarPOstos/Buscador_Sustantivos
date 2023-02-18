import streamlit as st


def set_style():
    """
    Simula lo que es el style.css de una pagina web debido a las limitaciones de streamlit y
    se va modificando la apariencia de la pagina
    """
    st.markdown("""<style>
    section.main.css-k1vhr4.egzxvld5 {
                    background-image: url("https://static.vecteezy.com/system/resources/previews/001/734/547/large_2x/seamless-pattern-of-open-books-vector.jpg");
                    background-size: cover;
                }
    .block-container.css-91z34k.egzxvld4 {
                    background-color: #ffffff;
                    border-radius: 20px
                }
    
    strong {font-size: 20px;}
    </style>""", unsafe_allow_html=True)
