def positionalintersect(p1,p2,k,invertedindex,tokenized):
    '''This function is for proximity intersection of postings lists p1 and p2. The function finds places where the two terms appear within k words of each other and returns a list of triples giving docID and the term position in p1 and p2.'''
    answer=list()
    shareddoc = set(invertedindex[p1]) & set(invertedindex[p2]) #Find the shared documents set
    for i in shareddoc :
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