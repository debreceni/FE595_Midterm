from textblob import TextBlob
from nltk.corpus import words
import nltk
import string
from collections import defaultdict


################ Service 1 ##################
def get_sentiment(text):
    try:
        sent = TextBlob(text).sentiment[0]
    except:
        sent = "Cannot determine sentiment."
    return float(str(sent))

################ Service 2 ##################
def translate(text):
    try:
        sent = TextBlob(text).translate(to = 'fr')
    except:
        sent = "This statement is invalid."
    return str(sent)

################ Service 3 ##################
def detect(text):
    try:
        sent=TextBlob(text).detect_language()
    except:
        sent = "Cannot determine language"
    return str(sent)


################ Service 4 ##################
def get_anagram(text):
    
    try:
        nltk.download('words')

        MIN_WORD_SIZE = 3

        testWords = text

        # Load the dictionary
        d = defaultdict(list)
        for word in words.words():
            key = "".join(sorted(word.lower().translate(str.maketrans('','',string.punctuation)))).strip()
            if len(key) >= MIN_WORD_SIZE:
                d[key].append(word.lower())
                d[key] = list(set(d[key]))

        #build a key for the test word
        testWordKey = "".join(sorted(testWords.lower().translate(str.maketrans('','',string.punctuation)))).strip()
        return d[testWordKey].remove(text)
    except:
        return None


################ Service 5 ##################


################ Service 6 ##################