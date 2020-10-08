import spacy

class Config(object):

    def __init__(self):
        self._nlp = spacy.load('en_core_web_md')

    @property
    def nlp(self):
        return self._nlp
