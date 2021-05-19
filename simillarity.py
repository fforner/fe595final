import spacy
import numpy as np
import re
from textblob import TextBlob
import pandas as pd
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
x = 'I am the best human in the word! I want beens.'

def similarity(x, word1 = 'good', word2 = 'bad'):
    ''' thanks to this funciton it is possible to comapare the similarity
     of all the names in the imput phrases and two words that i wnat.
    '''

    fra = TextBlob(x)
    a = pd.DataFrame(fra.tags)
    word1sim = []
    word2sim = []

    z = []
    for i in range(len(a)):
        if a.iloc[i,1] =='NN' or a.iloc[i,1] =='NNS':
            z.append(a.iloc[i,0].lower())
    npl_small = spacy.load('en_core_web_sm')
    for i in z:
        string =str(i)
        good = npl_small(word1).similarity(npl_small(string))
        bad = npl_small(word2).similarity(npl_small(string)) #do a similarity with bad
        word1sim.append((string, good))
        word2sim.append((string,bad))
    return word1sim,word2sim
    pass

            
