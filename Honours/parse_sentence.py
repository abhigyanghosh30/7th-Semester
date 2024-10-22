import pickle
from itertools import product
from collections import defaultdict
stopwords = {"अंदर", "अत", "अदि", "अप", "अपना", "अपनि", "अपनी", "अपने", "अभि", "अभी", "आदि", "आप", "इंहिं", "इंहें", "इंहों", "इतयादि", "इत्यादि", "इन", "इनका", "इन्हीं", "इन्हें", "इन्हों", "इस", "इसका", "इसकि", "इसकी", "इसके", "इसमें", "इसि", "इसी", "इसे", "उंहिं", "उंहें", "उंहों", "उन", "उनका", "उनकि", "उनकी", "उनके", "उनको", "उन्हीं", "उन्हें", "उन्हों", "उस", "उसके", "उसि", "उसी", "उसे", "एक", "एवं", "एस", "एसे", "ऐसे", "ओर", "और", "कइ", "कई", "कर", "करता", "करते", "करना", "करने", "करें", "कहते", "कहा", "का", "काफि", "काफ़ी", "कि", "किंहें", "किंहों", "कितना", "किन्हें", "किन्हों", "किया", "किर", "किस", "किसि", "किसी", "किसे", "की", "कुछ", "कुल", "के", "को", "कोइ", "कोई", "कोन", "कोनसा", "कौन", "कौनसा", "गया", "घर", "जब", "जहाँ", "जहां", "जा", "जिंहें", "जिंहों", "जितना", "जिधर", "जिन", "जिन्हें", "जिन्हों", "जिस", "जिसे", "जीधर", "जेसा", "जेसे",
             "जैसा", "जैसे", "जो", "तक", "तब", "तरह", "तिंहें", "तिंहों", "तिन", "तिन्हें", "तिन्हों", "तिस", "तिसे", "तो", "था", "थि", "थी", "थे", "दबारा", "दवारा", "दिया", "दुसरा", "दुसरे", "दूसरे", "दो", "द्वारा", "न", "नहिं", "नहीं", "ना", "निचे", "निहायत", "नीचे", "ने", "पर", "पहले", "पुरा", "पूरा", "पे", "फिर", "बनि", "बनी", "बहि", "बही", "बहुत", "बाद", "बाला", "बिलकुल", "भि", "भितर", "भी", "भीतर", "मगर", "मानो", "मे", "में", "यदि", "यह", "यहाँ", "यहां", "यहि", "यही", "या", "यिह", "ये", "रखें", "रवासा", "रहा", "रहे", "ऱ्वासा", "लिए", "लिये", "लेकिन", "व", "वगेरह", "वरग", "वर्ग", "वह", "वहाँ", "वहां", "वहिं", "वहीं", "वाले", "वुह", "वे", "वग़ैरह", "संग", "सकता", "सकते", "सबसे", "सभि", "सभी", "साथ", "साबुत", "साभ", "सारा", "से", "सो", "हि", "ही", "हुअ", "हुआ", "हुइ", "हुई", "हुए", "हे", "हें", "है", "हैं", "हो", "होता", "होति", "होती", "होते", "होना", "होने"}
hindi_doc = open('input.txt', 'r').readlines()
sentences = []


def get_rhyme_score(pair):
    word1 = pair[0]
    word2 = pair[1]
    i = len(word1)-1
    j = len(word2)-1
    count = 0
    while(word1[i] == word2[j] and i >= 0 and j >= 0):
        i -= 1
        j -= 1
        count += 1
    return count


def get_synonyms(word):
    word2Synset = pickle.load(
        open("python-hindi-wordnet/hindi_wordnet_python/WordSynsetDict.pk", 'rb'))
    synonyms = pickle.load(
        open("python-hindi-wordnet/hindi_wordnet_python/SynsetWords.pk", 'rb'))
    # word = word.decode('utf-8', 'ignore')
    if word in word2Synset:
        synsets = word2Synset[word]
        for pos in synsets.keys():
            for synset in synsets[pos]:
                if synset in synonyms:
                    return synonyms[synset]['1']


if __name__ == "__main__":
    synlists = []
    for sentence in hindi_doc:
        sentlist = []
        sentences.append(sentence.strip().split(' '))
        for words in sentence.strip().split(' '):
            if words not in stopwords:
                synwords = get_synonyms(words)
                if synwords is None:
                    sentlist.append([words])
                else:
                    sentlist.append(synwords)

            else:
                sentlist.append(None)
        synlists.append(sentlist)
    print(synlists)
    rhyming_score = defaultdict(int)
    rhyming_words = defaultdict()
    print(len(synlists[0]))
    print(len(synlists[1]))
    for i in range(len(synlists[0])):
        if synlists[0][i] is None:
            continue
        print(synlists[0][i])
        for j in range(len(synlists[1])):
            if synlists[1][j] is None:
                continue
            print(synlists[1][j])
            cart_p = product(synlists[0][i], synlists[1][j])
            for tpl in cart_p:
                score = get_rhyme_score(tpl)
                if score > rhyming_score[(i, j)]:
                    rhyming_score[(i, j)] = score
                    rhyming_words[(i, j)] = tpl
    print(rhyming_words)
    keymax = max(rhyming_words, key=rhyming_score.get)
    sentences[0][keymax[0]] = rhyming_words[keymax][0]
    sentences[1][keymax[1]] = rhyming_words[keymax][1]
    print(sentences)
