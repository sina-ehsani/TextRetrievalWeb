To run the program run run.sh from terminal.

It will ask for your search and it will find the answer.

You also have to rembemer the following instructions: 
1. If more than one operations are used, you have to add the parenthesis, it would not work without them. (i.e. treatment  or (schizophrenia and drugs)).
2. You can have multiple parentheses, but only one pair of search keys should be inside each parenthesis. 
4. There should not be parenthesis inside another parenthesis. 
5. All the parenthesis should be in the middle of the search, you can have single keywords, before or after all the parenthesis. (i.e. treatment  or (schizophrenia and drugs) and (treatment and drugs) and patients)

The process works in this way:
1. Does the operation inside all the parenthesis (if available).
2. It will operate from left to right for outside-parenthesis operations.

For example: 
treatment  or (schizophrenia and drugs) and (treatment and drugs) and patients
1. First, the program calculates both: (schizophrenia and drugs), (treatment and drugs)
2. It will start from left: treatment  or (schizophrenia and drugs)
3. Continues to right: treatment  or (schizophrenia and drugs) and (treatment and drugs) 
4. Until reaches the end: treatment  or (schizophrenia and drugs) and (treatment and drugs) and patients