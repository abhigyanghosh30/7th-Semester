import sys
import re
from nltk.stem import SnowballStemmer

stopwords = {'','redirect','nbsp','amp','the', 'myself', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'are', 'was', 'were', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'because', 'until', 'while', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'from', 'up', 'down', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'nor', 'not', 'only', 'own', 'same', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'}
st = SnowballStemmer('english')

titles = {}
rel_docs = []

def load_index(searchterm,cat):
    with open(searchterm[:2]+".txt") as indexfile:
        for line in indexfile.readlines():
            words = line.split(':')
            if words[0]!=searchterm:
                continue
            for item in words[1].split(','):
                nums = re.split('\D',item)
                types = re.split('\d+',item)
                #check if that category is in this doc
                if cat not in types:
                    continue
                count = nums[types.index(cat)]
                rel_docs.append({nums[0]:count})
            
                    

with open(sys.argv[1]) as inpf:
    line = inpf.readline()
    while line!= "":
        terms = re.split('\W',line)
        k = int(words[0])
        words = []
        for i in range(1,len(terms),2):
            words.append([terms[i],terms[i+1]])
        rel_docs = []
        for term in terms:
            #load all the indexes into the currindex
            if term[1] in stopwords:
                continue
            load_index(term[1],term[0])
        # sorted(rel_docs) do sorting of list here
        line= inpf.readline()                
