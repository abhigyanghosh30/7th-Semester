import os
sentences = []


def read_sentences():
    for file in os.listdir('training-hindi'):
        with open('training-hindi/'+file) as f:
            print(file)
            words = []
            currTag = []
            tags = []
            for line in f.readlines():
                line = line.strip()
                if line.startswith('</Sentence>'):
                    sentences.append(words)
                    continue
                if line.startswith('<Sentence'):
                    words = []
                    # tags = []
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


read_sentences()
with open('sentences.txt', 'w+') as f:
    for sentence in sentences:
        # print(sentence)
        f.write(" ".join(sentence))
        f.write("\n")
