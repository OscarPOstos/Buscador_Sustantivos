from nltk.tokenize import word_tokenize

nltk.download('punkt')


def set_indexes(text_file):
    estructura = {}
    key, texto = "", ""
    if len(text_file) == 6:
        for index in range(len(text_file)):
            if index % 2 == 0:
                key = text_file[index]
            else:
                texto = ",".join(word_tokenize(text_file[index])).replace(",", " ").replace("\n", " ")

            if key != "" and texto != "":
                estructura[key.lower()] = texto
                key, texto = "", ""

    return estructura
