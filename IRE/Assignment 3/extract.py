import nltk
from nltk.corpus import indian
from nltk.tag import tnt
import string
import os

pos_tagger = tnt.TnT()
sentences = []


def train_tagger():

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
    # tokenized = nltk.word_tokenize(sent_to_be_tagged)
    return pos_tagger.tag(sent_to_be_tagged)


def read_sentences():
    for file in os.listdir('training-hindi'):
        with open('training-hindi/'+file) as f:
            words = []
            currTag = []
            tags = []
            for line in f.readlines():
                line = line.strip()
                if line.startswith('</Sentence>'):
                    sentences.append([words, tags])
                    continue
                if line.startswith('<Sentence'):
                    words = []
                    tags = []
                    continue
                if line.startswith("<") or line == '':
                    continue
                attrs = line.split('\t')
                # print(attrs)

                if line[0].isdigit():
                    if attrs[1] == "((":
                        currTag.append(attrs[-1])
                    else:
                        words.append(attrs[1])
                        tags.append(currTag[-1])
                elif attrs[0] == "))":
                    currTag.pop()

    print(len(sentences))


read_sentences()
# train_tagger()
# for sent in sentences:
#     # sent.append(get_tags(sent[0]))
#     print(sent[0])
#     print(sent[1])
for sent in sentences:
    # print(sent[0])
    for i in range(len(sent[0])):
        if sent[1][i] != 'SSF':
            print(sent[0][i], sent[1][i])
