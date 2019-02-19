union(p1,p2)
while p1 != NIL and p2 != NIL 
do if docID(p1) = docID(p2)
	then ADD(answer, docID(p1))
	p1 <- next(p1)
	p2 <- next(p2)
else if docID(p1) < docID(p2)
	then ADD(answer, docID(p1))
	p1 <- next(p1)
else 
	then ADD(answer, docID(p2))
	p2 <- next(p2)
	
# When only one of the tokens is available in all of the documents:
while p1 != NIL
	ADD(answer, docID(p1))
	p1 <- next(p1)

while p2 != NIL
	ADD(answer, docID(p2))
	p2 <- next(p2)
return(answer)