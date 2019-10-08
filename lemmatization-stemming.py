import spacy
import nltk

# load spacy's English-language models
en_nlp = spacy.load('en')

# instantiate nltk's Porter Stemmer
stemmer = nltk.stem.PorterStemmer()


# define function to compare lemmatization in spacy with stemming in nltk
def compare_normalization(doc):
    # tokenize document in spacy
    doc_spacy = en_nlp(doc)
    # print lemmas found by spacy
    print("Lemmatization:\n{}".format([token.lemma_ for token in doc_spacy]))
    print("Stemming:\n{}".format([stemmer.stem(token.norm_.lower()) for token in doc_spacy]))


compare_normalization("Our meeting today was worse than yesterday, "
                      "I'm scared of meeting the clients tomorrow")
