from nltk import text
import pandas as pd
import re
from textblob import TextBlob
import textblob
from nltk import FreqDist

a = 'I am the best human in the word! I want beens.'

# Polarity 

def polarity(x):
    value = TextBlob(x).sentiment.polarity
    if value > 0.75:
        return 'Positive'
    elif value >=0.35 and value <= 0.75:
        return 'Neutral'
    else:
        return 'Negative'

# Frequency

f = ''
def frequency(x):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for i in x:
        if i not in punctuations:
            no_punct = no_punct + i
    l = list(no_punct.split(" "))
    f = FreqDist(l)
    return f.most_common(15)





