
import nltk
import string
import requests
from bs4 import BeautifulSoup


stop_words = set(nltk.corpus.stopwords.words("english"))
stop_words.update({'\'s', '\'re', 'n\'t'})
punctuation = set(string.punctuation)


def process_text(
        sent: str,
        stop_words: set = stop_words,
        punctuation: set = punctuation,
        lower=True) -> str:
    """
    Text processing function
    Arguments:
        - sent: string of the sentence to be cleaned
        - stop_words: set of common words to exclude
        - punctuation: set of punctuation marks to exclude
        - lower: boolean, produce lower case
    Returns:
        - cleaned tokenized sentences
    """
    words_unclean = nltk.word_tokenize(sent)
    words = [word for word in words_unclean if word not in punctuation]
    words_clean = [word for word in words if word not in stop_words]
    if lower:
        words_clean = [word.lower() for word in words_clean]
    return " ".join(words_clean)


def extract_text_from_url(url: str) -> str:
    """
    Arguments:
        - url: string
    Returns:
        - text: string from the url's page
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    paragraphs = soup.find_all("p")
    text = " ".join([p.get_text() for p in paragraphs])

    return text

