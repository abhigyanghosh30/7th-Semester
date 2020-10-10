import nltk
from nltk.corpus import indian
from nltk.tag import tnt
import string
import os

pos_tagger = tnt.TnT()
sentences = []


def train_tagger():
    nltk.download('punkt')
    nltk.download()

    tagged_set = 'hindi.pos'
    word_set = indian.sents(tagged_set)
    data = indian.tagged_sents(tagged_set)

    count = 0
    for sen in word_set:
        count = count + 1
        sen = "".join([" "+i if not i.startswith("'")
                       and i not in string.punctuation else i for i in sen]).strip()
        print(sen)
    print(count)

    train_perc = .9

    train_rows = int(train_perc*count)
    test_rows = train_rows + 1

    print(train_rows, test_rows)

    data = indian.tagged_sents(tagged_set)
    train_data = data[:train_rows]
    test_data = data[test_rows:]

    pos_tagger.train(train_data)
    pos_tagger.evaluate(test_data)


def get_tags(sent_to_be_tagged):
    tokenized = nltk.word_tokenize(sent_to_be_tagged)
    return pos_tagger.tag(tokenized)


def read_sentences():
    for file in os.listdir():
        with open(file) as f:
            sentences = []
            words = []
            currTag = []
            tags = []
            for line in f.readlines():
                if line.startswith('</Sentence>'):
                    sentences.append((words, tags))
                elif line.startswith('<Sentence'):
                    words = []
                    tags = []

                attrs = line.split('\t')
                if attrs[1] == "((":
                    currTag.append(attrs[3])
                elif attrs[1] == "))":
                    currTag.pop()
