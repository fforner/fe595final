import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
import os
#reference link: https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da

def pos_tagging(sent):
    article = nlp(sent)
    labels = [x.label_ for x in article.ents]
    items = [x.text for x in article.ents]
    sentences = [x for x in article.sents]
    #displacy.render(nlp(str(sentences[20])), jupyter=True, style='ent')
    #displacy.render(nlp(str(sentences[20])), style='dep', jupyter=True, options={'distance': 120})
    #dict([(str(x), x.label_) for x in nlp(str(sentences[20])).ents])
    #print([(x, x.ent_iob_, x.ent_type_) for x in sentences[20]])
    svg = displacy.render(article, page=True, style='ent')
    return svg
