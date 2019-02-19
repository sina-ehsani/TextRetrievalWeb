# p1 OR NOT p2
ornot(p1,p2):
m=1

while p1 != NIL and p2 != NIL 
	p2 <- 0 # We start with 0, this will force the algorithm to count all the documents before either p1 or p2 
	
	if docID(p2) < docID(p1)
		for i in [docID(p1)-docID(p2)]
			while docID(p2+i) < docID(next(p2))
				ADD(answer, docID(p2+i))
				i++
		p2 <- next(p2)
	else
		ADD(answer, docID(p1))
		p1 <- next(p1)

# When only one of the tokens is available in all of the documents:
while p1 != NIL
	for i in count(docID)
		ADD(answer, docID(i))

while p2 != NIL
	while(docID(m)<docID(p2)
		ADD(answer, docID(m))
		m++
	p2 <- next(p2)
		
return(answer)