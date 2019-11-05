from textblob import TextBlob
from nltk.corpus import words
import nltk
import string
from collections import defaultdict
nltk.download('words')

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



################ Service 5 ##################


################ Service 6 ##################
def get_anagram(text):
    
    try:
        MIN_WORD_SIZE = 3
        testWords = text.lower()

        # Load the dictionary
        d = defaultdict(list)
        for word in words.words():
            key = "".join(sorted(word.lower().translate(str.maketrans('','',string.punctuation)))).strip()
            if len(key) >= MIN_WORD_SIZE:
                d[key].append(word.lower())
                d[key] = list(set(d[key]))

        #build a key for the test word
        testWordKey = "".join(sorted(testWords.lower().translate(str.maketrans('','',string.punctuation)))).strip()
        return [w for w in d[testWordKey] if w != text.lower()]
    except:
        return None