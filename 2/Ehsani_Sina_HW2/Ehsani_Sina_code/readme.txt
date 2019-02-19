To run the program run run.sh from terminal.

It will ask for your search query, it will find proximity intersection of postings lists word1 and word2. The program finds places where the two terms appear within k words (it also has support for directional queries) of each other and returns a list of triples in the following format: (docID, term position of word1, term position of word2.)

You also have to remember the following instructions: 
1. You should type your query in the following format: "word1 /k word2" (backslash before the number is necessary)
2. Then the program will ask whether if you want the directional positional intersect or the regular one. To indicate that you want the directional one type "a". Any other input will return the nondirectional results.