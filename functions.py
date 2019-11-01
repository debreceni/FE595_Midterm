from textblob import TextBlob


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