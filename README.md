# Lemmatization and Stemming

Suppose if we have same words in vocabulary like "drawing", "drawbacks", "drawers" and "drawers". For the
purposes of a bag-of-words model, the semantics of "drawback" or "drawbacks" are so close that distinguishing
between them will only increase overfitting, and not allow the model to fully exploit the training data.

## Solutions

The problem can be overcome by representing each word using its _word stem_, which involves identifying (or
_conflating_) all the words that have the same word stem.

### Stemming

If this is done by using rule-based heuristic, like dropping common suffixes, it is called as stemming.

### Lemmatization

If instead a dictionary of known word forms is used, and the role of the word in the sentence is taken 
into account, the process is called lemmatization.

## Example

```sh
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

```

Output:
```sh
Lemmatization:
['-PRON-', 'meeting', 'today', 'be', 'bad', 'than', 'yesterday', ',', '-PRON-', 'be', 'scared', 'of', 'meet', 'the', 'client', 'tomorrow']
Stemming:
['our', 'meet', 'today', 'wa', 'wors', 'than', 'yesterday', ',', 'i', 'am', 'scare', 'of', 'meet', 'the', 'client', 'tomorrow']
```

### Conclusion
Stemming is always restricted to trimming the word to a stem, so "was" becomes "wa", while lemmatization can retrieve
the correct base verb form, "be". Similarly, lemmatization can normalize "worse" to "bad", while stemming produces
"wors".