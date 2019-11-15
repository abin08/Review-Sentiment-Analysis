import pandas as pd
import numpy as np
import spacy
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
import re
from contractions import CONTRACTION_MAP

sp = spacy.load('en', parse=True, tag=True, entity=True)
tokenizer = ToktokTokenizer()
stopwords_list = nltk.corpus.stopwords.words('english')

def expand_contractions(text, c_map = CONTRACTION_MAP):
    words = text.split()
    expanded_words_list = [c_map[word] if word in c_map else word for word in words]
    expanded_text = ' '.join(expanded_words_list)
    return expanded_text

def remove_special_chars(text, remove_digits=False):
    """
    Removes special characters from text using regular expression, also
    removes digits if remove_digits is True
    """
    try:
        pattern = r'[^a-zA-Z0-9\s]' if not remove_digits else r'[^a-zA-Z\s]'
        text = re.sub(pattern, '', text)
    except TypeError:
        pass
    return text

def lemmatize_text(text):
    """
    Lemmatize the words using spacy
    Note: Pronouns are excluded (eg: he, she, my, it etc...)
    """
    try:
        text = sp(text)
        text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
    except TypeError:
        pass
    return text

def remove_stopwords(text):
    """
    Removes stopwords from the text using nltk stopwords_list
    """
    tokens = get_tokens(text)
    filtered_tokens = [token for token in tokens if token not in stopwords_list]
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text

def get_tokens(text):
    """
    Converts text to a list of tokens using nltk tokenizer
    """
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    return tokens

def clean_text(text, contraction_expansion=True, special_chars_removal=True, stemming=True, 
    lemmatization=True, stopwords_removal=True, remove_digits=True):
    """
    Performs text preprocessing methods on the text based on true arguments
    """
    text = text.lower()
    if contraction_expansion:
        text = expand_contractions(text)
    if special_chars_removal:
        text = remove_special_chars(text, remove_digits=remove_digits)
    if lemmatization:
        text = lemmatize_text(text)
    if stopwords_removal:
        text = remove_stopwords(text)
    return text
