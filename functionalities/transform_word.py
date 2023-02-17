import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
def remove_stopwords(text):
    return ' '.join([word for word in text.split() if word not in stopwords.words("spanish")])
