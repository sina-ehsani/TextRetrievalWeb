
# coding: utf-8

# In[9]:

import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
unionwords = ['or','and']
result=dict()

def union2(p1,p2):
    '''This def will return the union of two binary searches''' 
    L3 = [max(l1, l2) for l1, l2 in zip(p1, p2)]
    return(L3)
def intersection2(p1,p2):
    '''This def will return the intersection of two binary searches'''
    L3 = [min(l1, l2) for l1, l2 in zip(p1, p2)]
    return(L3)
def tokenize(search):
    '''This def tokenize, lower csae, and stem all the strings'''
    search_token = word_tokenize(search) #Tokenize
    search_token = [i.lower() for i in search_token] # Lower Case
    search_token = [porter.stem(word) for word in search_token] #Stem
    return(search_token)
def extractkeys(tokens , mydict):
    '''This token will extract the operation sumbols and match the keys of each tokens with our binary matrix'''
    unionwords = ['or','and']
    operations = [word for word in unionwords if word in tokens] #operation
    keys = [word for word in tokens if word not in unionwords and word in [*mydict.keys()]] #keys
    return(operations, keys)
def operation(p1,p2,operation):
    '''This def does the union and intersection, given the binary data, and the operation types (or, and)'''
    out=list()
    if operation == ['or']:
        out=union2(p1,p2)
    elif operation == ['and']:
        out=intersection2(p1,p2)
    return(out)


def prepro(docs):
    ''' This is the preprocessing module, whitch given a txt document that each new line is one document, and each line starts with the documentID. 
    This Def will return the term-document incidence matrix'''
    infile = open(docs,'r')
    docs=infile.readlines()
    docs=[i.strip() for i in docs] #removing the \n
    docs=[i.lower() for i in docs] #Lower Case

    tokenized = [word_tokenize(docs[i]) for i in range(len(docs))]
    [i.pop(0) for i in tokenized] # Removing the ID

    porter = PorterStemmer()
    stemmed=[]
    for i in range(len(docs)):
        stem = [porter.stem(word) for word in tokenized[i]]
        stemmed.append(stem)

    tokens = set(x for l in stemmed for x in l)
    mydict = dict()
    for el in tokens:
        mydict[el]=[stemmed[i].count(el) for i in range(len(docs))]
    return(mydict)

def process2(search,mydict):
    '''This def, takes the operation search (i.e. patiens and drugs), and term-document incidence matrix and finds the search result. The search results are shown in a binary list, which each value of this arry represent document (starting from the 1st document to the last.)'''
    inside=re.findall('\((.*?)\)',search)
    outside = re.findall('\)(.*?)\(',search)
    search_token = tokenize(search)
    operations, search_keys = extractkeys(search_token,mydict)

    if len(search_keys)==1:
        result['operat']=mydict[search_keys[0]]
    if len(search_keys)==2:  
        result['operat']=operation(mydict[search_keys[0]],mydict[search_keys[1]],operations)

    if len(search_keys) > 2:
        for i in range(len(inside)):
            tokens = tokenize(inside[i])
            operations_inside, keys_inside = extractkeys(tokens,mydict)
            result[i]=operation(mydict[keys_inside[0]],mydict[keys_inside[1]],operations_inside)
        
        #First:
        if search_token[0]!='(':
            result['operat']=operation(result[0], mydict[search_token[0]],[search_token[1]])
        else:
            result['operat']=result[0]
        #Middle:
        
        if outside:
            operations_outside = [tokenize(i) for i in outside]
            for j in range(0,len(operations_outside)):
                result['operat'] = operation(result['operat'], result[j+1],operations_outside[j])
        #Last:    
        if search_token[-1]!=')':
            result['operat']=operation(result['operat'], mydict[search_token[-1]],[search_token[-2]])
    return(result['operat'])


def submain(docs = "docs.txt"):


    search=input("give the operation:")
    mydict = prepro(docs)
    result = process2(search,mydict)
    print(result)
    return(result)

def main():
    while True:
        submain()

if __name__ == '__main__':
    main()

