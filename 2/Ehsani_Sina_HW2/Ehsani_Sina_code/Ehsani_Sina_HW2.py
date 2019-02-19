
# coding: utf-8

# In[9]:

import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()

def invertindex(docs="docs.txt"):
    '''This fundtion will take the document txt folder (each line should indicate new document and the first token is document name)
    It will return the inverted index and the tokenized (and stemed) version of all the documents'''
    stemmed=[]
    infile = open(docs,'r')
    docs=infile.readlines()
    docs=[i.strip() for i in docs] #removing the \n
    docs=[i.lower() for i in docs] #Lower Case
    tokenized = [word_tokenize(docs[i]) for i in range(len(docs))]
    [i.pop(0) for i in tokenized] # Removing the ID
    for i in range(len(docs)):
        stem = [porter.stem(word) for word in tokenized[i]]
        stemmed.append(stem)
    index=dict()
    for i in range(len(stemmed)):
        for word in set(stemmed[i]):
            if word in index:
                index[word].append(i+1)
            else:
                index[word]=[i+1]
    return(index,stemmed)

def positionalintersect(p1,p2,k,invertedindex,tokenized):
    '''This function is for proximity intersection of postings lists p1 and p2. The function finds places where the two terms appear within k words of each other and returns a list of triples giving docID and the term position in p1 and p2.'''
    answer=list()
    shareddoc = set(invertedindex[p1]) & set(invertedindex[p2]) #Find the shared documents set
    for i in shareddoc :
    #     p1index=tokenized[i-1].index(p1)
    #     p2index=tokenized[i-1].index(p2)   
        p1indices = [i for i, x in enumerate(tokenized[i-1]) if x == p1]
        p2indices = [i for i, x in enumerate(tokenized[i-1]) if x == p2]
        l=list()
        for pp1 in p1indices:
            for pp2 in p2indices:
                while True:
                    if abs(pp1-pp2) <= k:
                        l.append(pp2)
                    elif pp2 > pp1:
                        break
                    while len(l)!=0 and abs(l[-1] - pp1) > k:
                        l.pop()
                    for s in l:
                        answer.append((i, pp1, s))
                    break
    return(answer) 

def positionalintersect2(p1,p2,k,invertedindex,tokenized):
    '''This function is modified version of the positionalintersect function.
    which means given the query word1 /k word2 is will return occurrences of word1 strictly before word2, within k words.'''

    answer=list()
    shareddoc = set(invertedindex[p1]) & set(invertedindex[p2]) #Find the shared documents set
    for i in shareddoc :
    #     p1index=tokenized[i-1].index(p1)
    #     p2index=tokenized[i-1].index(p2)   
        p1indices = [i for i, x in enumerate(tokenized[i-1]) if x == p1]
        p2indices = [i for i, x in enumerate(tokenized[i-1]) if x == p2]
        l=list()
        for pp1 in p1indices:
            for pp2 in p2indices:
                while True:
                    if 0 < pp2-pp1 <= k:
                        l.append(pp2)
                    elif pp1 > pp2:
                        break
                    elif pp2 > pp1:
                        break
                    while len(l)!=0 and abs(l[-1] - pp1) > k:
                        l.pop()
                    for s in l:
                        answer.append((i, pp1, s))
                    break
    return(answer)     

def querytokenizer(query):
    '''Given query with following formt: "p1 /k p2"
    This function will return stemed strings of p1 and p2, and k as a intiger'''
    search_token = word_tokenize(query) #Tokenize
    search_token = [i.lower() for i in search_token] # Lower Case
    search_token = [porter.stem(word) for word in search_token] #Stem
    #Extract k
    r = re.compile("\/\d+")
    m = r.findall(query)
    k=int(m[0].replace("/", ""))
    p1=search_token[0]
    p2=search_token[-1]
    return(p1,p2,k)


def submain(docs = "docs.txt"):
    query=input("Please give me the query (format: p1 /k p2)")
    qtype=input("Which type of query do you want? (type 'a' for the directional positional intersect (part2), otherwise it will use regular positional intersect (part 1))")
    invertedindex,tokenized =invertindex(docs)
    p1,p2,k = querytokenizer(query)
    if qtype == "a":
        answer=positionalintersect2(p1,p2,k,invertedindex,tokenized)
    else:
        answer=positionalintersect(p1,p2,k,invertedindex,tokenized)
    print(answer)
    return(answer)

def main():
    while True:
        submain()


if __name__ == '__main__':
    main()