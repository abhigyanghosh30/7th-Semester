import sys
import re
import math
from nltk.stem import SnowballStemmer
import pickle

stopwords = {'','redirect','nbsp','amp','the', 'myself', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'are', 'was', 'were', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'because', 'until', 'while', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'from', 'up', 'down', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'nor', 'not', 'only', 'own', 'same', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'}
st = SnowballStemmer('english')

titles = {}
rel_docs = {}
counts = {}


with open('totaltitle.pickle','rb') as titlefile:
    titles=pickle.load(titlefile)

ndocs = len(titles.keys())

def tf_idf(countword,countdoc):
    return (1+math.log(countword))*(ndocs/countdoc)

def load_index(searchterm,cat):
    #print(searchterm,cat)
    with open(searchterm[:2]+".txt") as indexfile:
        if searchterm not in rel_docs:
            rel_docs[searchterm]=set()
        for line in indexfile.readlines():
            words = line.split(':')
            if words[0]!=searchterm:
                continue
            r_docs = words[1].split(',')
            for item in r_docs:
                nums = re.split('\D',item)
                types = re.split('\d+',item)
                #check if that category is in this doc
                if cat not in types:
                    continue
                #print(searchterm,cat, titles[nums[0]])
                count = int(nums[types.index(cat)])
                rel_docs[searchterm].add(nums[0])
                counts[nums[0]]=tf_idf(count,len(r_docs))
            return


with open(sys.argv[1]) as inpf:
    line = inpf.readline()
    while line!= "":
        terms = re.split(',\s|:|\s',line)
        k = int(terms[0])
        words = {}
        currind = terms[1]
        for i in range(1,len(terms)):
            if len(terms[i])==1:
                words[terms[i]]=[]
                currind=terms[i]
            else:
                words[currind].append(terms[i])
        rel_docs = {}
        counts = {}
        for types in words:
            for word in words[types]:
                if word in stopwords:
                    continue
                load_index(st.stem(word.lower()),types)

        l = 0
        keys = list(rel_docs.keys())
        #print(len(keys))
        #print(len(rel_docs[keys[0]]))
        inter = rel_docs[keys[0]]
        for i in keys:
            # print(i)
            inter = inter.intersection(rel_docs[i])
        inter = list(inter)
        # print(len(inter))
        inter.sort(key=lambda x: counts[x], reverse=True)
        for item in inter:
            if titles[item]=="Template" or  titles[item]=='Wikipedia' or titles[item]=='Category':
                continue
            print(item+", ",titles[item])
            l+=1
            if l==k:
                break
        line= inpf.readline()

