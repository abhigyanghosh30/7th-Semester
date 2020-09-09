from nltk.stem import SnowballStemmer
import xml.sax
import pickle
import re
from nltk import RegexpTokenizer
import sys
title = {}
index = {} #t:title,b:body,c:category,r:references,l:links
stem_cache = {}
stopwords = {'','redirect','nbsp','amp','the', 'myself', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'are', 'was', 'were', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'because', 'until', 'while', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'from', 'up', 'down', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'nor', 'not', 'only', 'own', 'same', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'}
st = SnowballStemmer('english')
tokenizer = RegexpTokenizer("[a-zA-Z0-9]+")

def stem_word(word):
    word=word.lower()
    if word not in stem_cache:
        stem_cache[word] = st.stem(word)
    return stem_cache[word]

class DocHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentData = ""
        self.id = ""
        self.subindex={}
        self.links=False
        self.count=0

    def mergeindex(self):
        title[self.id]=self.title
        self.links=False
        for key in self.subindex:
            temp = self.id
            if key not in index:
                index[key]=list()
            # print(index[key])
            for j in self.subindex[key]:
                temp+=j
                temp+=str(self.subindex[key][j])
            index[key].append(temp)
        
    def add_to_index(self,word, item):
        if word not in self.subindex:
            self.subindex[word]={}
        if item not in self.subindex[word]:
            self.subindex[word][item]=1
        self.subindex[word][item]+=1

    def parsetext(self,content):
        if "External links" in content:
            self.ref = True
            return
        if self.links==True:
            for word in tokenizer.tokenize(content.strip()):
                self.count+=1
                if word in stopwords or len(word)<=3:
                    continue
                word = stem_word(word)
                self.add_to_index(word,"l")
        elif "[[Category" == content[:11]:
            for word in tokenizer.tokenize(content[11:-2]):
                self.count+=1
                if word in stopwords or len(word)<=3:
                    continue
                word = stem_word(word)
                self.add_to_index(word,"c")
        elif content[:9]=="{{Infobox":
            for word in tokenizer.tokenize(content[9:].strip()):
                self.count+=1
                if word in stopwords or len(word)<=3:
                    continue
                word = stem_word(word)
                self.add_to_index(word,"i")
        elif content.startswith('|'):
            attr = content.split('\=')
            if len(attr)>1:
                for word in tokenizer.tokenize(attr[1]):
                    self.count+=1
                    if word in stopwords or len(word)<=3:
                        continue
                    word = stem_word(word)
                    self.add_to_index(word,"i")
        elif content[:2]=="}}" or content[:2]=="==":
            pass
        elif "cite" in content:
            cites = re.findall("{{[Cc]ite(.+?)}}",content)
            for cite in cites:
                for word in tokenizer.tokenize(cite.strip()):
                    self.count+=1
                    if word in stopwords or len(word)<=3:
                        continue
                    word = stem_word(word)
                    self.add_to_index(word,"r")
        else:
            for word in tokenizer.tokenize(content.strip()):
                self.count+=1
                if word in stopwords or len(word)<3:
                    continue
                word = stem_word(word)
                self.add_to_index(word,"b")


    def startElement(self, tag, attributes):            
        self.currentData = tag
        if tag == 'page':
            self.currentData = ""
            self.id = ""
            self.subindex={}
            
    def characters(self, content):
        content = content.strip()
        if self.currentData == "title":
            self.title=content
            for word in tokenizer.tokenize(content):
                word = stem_word(word)
                self.add_to_index(word,'t')
        elif self.currentData == "text":
            self.parsetext(content)
        elif self.currentData == "id":
            if self.id=="":
                self.id = content

    def endElement(self, tag):
        if tag =="page":
            self.mergeindex()
        self.currentData=""
        

parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = DocHandler()
parser.setContentHandler( Handler )
parser.parse(sys.argv[1])

fp = open(sys.argv[2],'w+')
for key in sorted(index.keys()):
    fp.write(key)    
    fp.write(":")
    fp.write(",".join(index[key]))    
    fp.write("\n")
fp.close()
fp = open(sys.argv[2]+'title','w+')
for t in title:
    fp.write(t)
    fp.write(":")
    fp.write(title[t])
    fp.write("\n")
fp.close()
fp = open(sys.argv[3],'w+')
fp.write(str(len(index)))
fp.write(str(Handler.count))
