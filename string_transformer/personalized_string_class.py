import nltk
import unidecode
from nltk.corpus import stopwords

nltk.download('stopwords')


class PersonalizedStringClass:

    def __init__(self, text):
        self.text = text

    def lower_text(self):
        self.text = self.text.lower()
        return self

    def normalize_text(self):
        self.text = unidecode.unidecode(self.text)
        return self

    def remove_stopwords(self):
        self.text = ' '.join([word for word in self.text.split()
                              if word not in stopwords.words("spanish")])
        return self
