from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from tesaurus import *
import re
import sys
from regex import *
from KMP_BM import *

fQnA = open('QnA.txt', 'r')#readfile
listOfQnA = [[word.rstrip('\n').strip() for word in line.split('?')] for line in fQnA]

query = ""
for i in range(len(sys.argv)-1):
    query += sys.argv[i+1] + " "

query=query.strip().rstrip('?')

splitBySpace = query.split(" ")
isRegex = False
i = 0
while (i < len(splitBySpace) and not isRegex):
    isRegex = not splitBySpace[i].isalnum()
    i += 1
if (isRegex):
    Regex(query)
else:
    solveQuery(query)