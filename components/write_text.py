def write_text(text):
    html_result = "<p>"
    for word in text:
        if word[1].startswith("nc"):
            html_result += " <strong>" + word[0] + "</strong>"
        elif word[1] == "Fp":
            html_result += word[0]
        else:
            html_result += " " + word[0]
    html_result += "</p>"
    st.markdown(html_result, unsafe_allow_html=True)
