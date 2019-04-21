from tesaurus import *
import re

def regexAddSynonim(idx,start, end,query, word):
    sinonim = getSinonim(word)
    addedWords  = "("
    for i in range(len(sinonim)):
        addedWords = addedWords[:len(addedWords)] + sinonim[i]
        if (i <len(sinonim) -1):
            addedWords = addedWords[:len(addedWords)] + "|"
    addedWords = addedWords[:len(addedWords)] + ")"
    query = query[:start] + addedWords + query[end:]
    idx += len(addedWords) - len(word)
    return {
        'query' : query,
        'idx' : idx
    }


def Regex(query):
    query = query.lower()
    length = len(query)
    i = 0
    startIdx = -1
    endIdx = -1
    while (i < len(query)):
        if (query[i].isalpha()):
            if (startIdx == -1):
                startIdx = i
        elif (startIdx != -1) :
            endIdx = i
            res = regexAddSynonim(i, startIdx, endIdx, query, query[startIdx:endIdx])
            query = res['query']
            i = res['idx']
            startIdx = -1
        i += 1
    idxMatchedQuestion = []
    for i in range (len(listOfQnA)):
        x = re.search(query, listOfQnA[i][0], flags = re.IGNORECASE)
        if (x != None and len(idxMatchedQuestion)<3):
            idxMatchedQuestion.append(i)
    if(len(idxMatchedQuestion)==1):
        print(listOfQnA[idxMatchedQuestion[0]][1])
    else:
        for i in range (len(idxMatchedQuestion)):
            print('- '+listOfQnA[idxMatchedQuestion[i]][0]+'?')
    print('regex') 

fQnA = open('QnA.txt', 'r')#readfile
listOfQnA = [[word.rstrip('\n').strip() for word in line.split('?')] for line in fQnA]
