from nltk import text
import pandas as pd
import re
from textblob import TextBlob
import textblob
from nltk import FreqDist

a = 'I am the best human in the word! I want beens.'

# subjectivity 

def subjectivity(x):
    value = TextBlob(x).sentiment.subjectivity
    if value > 0.75:
        print('Positive')
    elif value >=0.35 and value <= 0.75:
        print('Neautral')
    else:
        print('Negative')
    return value


