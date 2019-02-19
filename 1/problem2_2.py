# p1 AND NOT p2

andnot(p1,p2)
while p1 != NIL and p2 != NIL 
do if docID(p1) = docID(p2)
	p1 <- next(p1)
	p2 <- next(p2)
else if docID(p1) < docID(p2)
	then ADD(answer, docID(p1))
		p1 <- next(p1)
else 
	p2 <- next(p2)
	
# When p2 is not available in the documents:
while p1 != NIL and p2 = NIL
	ADD(answer, docID(p1))
	p1 <- next(p1)
return(answer)