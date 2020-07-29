import numpy as np
import nltk
import string
import os
from nltk import data
from nltk.corpus import reuters

data.path.append(r'c:\nltk_data')  

def get_tokens():
   with open('C:/Users/xn/BigDataAnalytics/TF-IDF/shake1.txt', 'r') as shakes:
    text = shakes.read()
    lowers = text.lower()
    #remove the punctuation using the character deletion step of translate
    no_punctuation = lowers.translate(string.punctuation)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

tokens = get_tokens()