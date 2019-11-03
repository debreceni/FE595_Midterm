from textblob import TextBlob
import spacy

nlp = spacy.load("en_core_web_sm")
# Tags collected from https://spacy.io/api/annotation#pos-tagging
SPACY_POS_MAPPING = {
    'adjective': ['ADJ'],
    'verb': ['VERB', 'AUX'],
    'noun': ['NOUN', 'PROPN'],
    'pronoun': ['PRON'],
    'adverb': ['ADV'],
    'preposition': ['ADP'],
    'conjunction': ['CONJ', 'CCONJ', 'SCONJ'],
    'interjection': ['INTJ'],
    'determiner': ['DET'],
    'number': ['NUM'],
    'symbol': ['SYM'],
    'other': ['X', 'PUNCT', 'SPACE', 'PART']
}


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
        sent = TextBlob(text).translate(to='fr')
    except:
        sent = "This statement is invalid."
    return str(sent)


################ Service 3 ##################
def detect(text):
    try:
        sent = TextBlob(text).detect_language()
    except:
        sent = "Cannot determine language"
    return str(sent)


################ Service 4 ##################
def getPOS(text, tag):
    """
    SERVICE 1: Extracts one given part-of-speech from given text
    :param text: the text to search in
    :param tag: which tag to search for (regular word or actual POS code)
    :return: All the words in the text that match the part-of-speech to look for
    """
    text = nlp(text)
    pos = [(token.text, token.pos_) for token in text]
    result = [word[0] for word in pos if word[1] in [tag] + (SPACY_POS_MAPPING.get(tag) or [])]
    return ', '.join(result)


################ Service 5 ##################
def getSimilarity(s1, s2):
    """
    SERVICE 2: Gives the cosine similarity between any two given texts
    Note: This service uses small spaCy model because of AWS EC2 RAM constraints, so results are different compared to the larger models.
    :param s1, s2: the texts to calculate the similarity of
    :return: The cosine similarity of two given text strings
    """
    def filterText(text):
        """Remove stopwords, pronouns, and punctuation"""
        result = [t for t in nlp(text.lower()) if t.text not in nlp.Defaults.stop_words]  # - stopwords
        result = [t for t in result if t.lemma_ != '-PRON-']  # - pronouns
        return ' '.join([t.text for t in result if not t.is_punct])  # - punctuation
    return round(nlp(filterText(s1)).similarity(nlp(filterText(s2))), 4)


################ Service 6 ##################
