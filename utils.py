import nltk
import string


stop_words = set(nltk.corpus.stopwords.words("english"))
stop_words.update({'\'s', '\'re', 'n\'t'})
punctuation = set(string.punctuation)


def process_text(sent: str, stop_words: set = stop_words, punctuation: set = punctuation) -> str:
    words_unclean = nltk.word_tokenize(sent)
    words = [word for word in words_unclean if word not in punctuation]
    words_clean = [word for word in words if word not in stop_words]
    return " ".join(words_clean)
