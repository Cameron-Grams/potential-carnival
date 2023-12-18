import nltk
import string
import requests
from bs4 import BeautifulSoup

from other_text import non_wiki

stop_words = set(nltk.corpus.stopwords.words("english"))
stop_words.update({'\'s', '\'re', 'n\'t'})
punctuation = set(string.punctuation)

# change or modify to select sample articles
reference_texts = [ ('Shakespeare', 'https://en.wikipedia.org/wiki/William_Shakespeare'),
			('Voltaire', 'https://en.wikipedia.org/wiki/Voltaire'),
			('Abraham_Lincoln', 'https://en.wikipedia.org/wiki/Abraham_Lincoln'),
			('Hydrogen_Economy', 'https://en.wikipedia.org/wiki/Hydrogen_economy'),
			('Coal', 'https://en.wikipedia.org/wiki/Coal'),
			('Nuclear_power', 'https://en.wikipedia.org/wiki/Nuclear_power'),
            ('Biden_deposition', 'https://www.pbs.org/newshour/politics/house-republicans-reiterate-their-demand-for-hunter-biden-to-appear-for-a-private-deposition')]
     

def text_into_sentences(text: str) -> list[str]:
    sentences = nltk.sent_tokenize(text)
    return sentences


def process_sentences_text(
        sent: str,
        stop_words: set = stop_words,
        punctuation: set = punctuation,
        lower=True) -> str:
    """
    Text processing function for sentences

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


def produce_example_corpus(reference_texts=reference_texts, non_wiki=non_wiki):
    """
    Produces a list of tokenized text and the document titles
    arguments:
        - reference_texts: list of tuples; (title, url)
        - non_wiki: list of tuples; (title, text strin)
    returns: 
        - processed_text_strings: list of tokenized strings
        - text_titles: list of document titles
    """
    processed_text_strings = []
    text_dictionary = {}
    for tpc, url in reference_texts:
        text_dictionary[tpc] = extract_text_from_url(url)

    unprocessed_text_strings = list(text_dictionary.values())
    unprocessed_text_strings.extend([t[1] for t in non_wiki])

    document_titles = list(text_dictionary.keys())
    document_titles.extend([t[0] for t in non_wiki])

    # List of text stringprocessed_text_strings = []
    for text in unprocessed_text_strings:
        new_sentences = []
        sentences = nltk.sent_tokenize(text)
        for sent in sentences:
            cleaned_sent = process_sentences_text(sent)
            new_sentences.append(cleaned_sent)
        new_text = " ".join(new_sentences)
        processed_text_strings.append(new_text)

    return processed_text_strings, document_titles
