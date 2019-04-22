import sys
from regex import *
from KMP_BM import *

fQnA = open('QnA.txt', 'r')#readfile
listOfQnA = [[word.rstrip('\n').strip() for word in line.split('?')] for line in fQnA]



query = ""
for i in range(2,len(sys.argv)):
    query += sys.argv[i] + " "
query=query.strip().rstrip('?')

splitBySpace = query.split(" ")

if(sys.argv[1]=="exact"):
    solveQuery(query)
else:
    Regex(query)