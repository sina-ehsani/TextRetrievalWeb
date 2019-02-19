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