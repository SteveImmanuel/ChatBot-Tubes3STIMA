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

def deleteStopWord(pattern, listOfStopWord):
#clean the received string
    
    temp=pattern.split(' ')
    for word in listOfStopWord:
        try:
            temp.remove(word)
        except:
            continue
    temp=' '.join(temp)
    return temp

def removeStopRegex(query, listOfStopWord):
    i = 0
    startIdx = 0
    endIdx = 0
    while (i < len(query)):
        if (query[i].isalpha()):
            if (startIdx == -1):
                startIdx = i
            elif (i == len(query)-1):
                endIdx = i+1
                for word in listOfStopWord:
                    if (query[startIdx:endIdx] == word):
                        query = query[:startIdx] + query[endIdx:]
                        i = startIdx-1
                        break;
                startIdx = -1
        elif (startIdx != -1):
            endIdx = i
            for word in listOfStopWord:
                if (query[startIdx:endIdx] == word):
                    query = query[:startIdx] + query[endIdx:]
                    i = startIdx-1
                    break;
            startIdx = -1
        i += 1
    return query

def Regex(query):
    query = query.lower()
    fStopWord = open('StopWord.txt', 'r')#readfile
    listOfStopWord = [line.rstrip('\n') for line in fStopWord]
    dummy = [None for i in range(len(listOfQnA))]
    for i in range(len(listOfQnA)):
        dummy[i]=listOfQnA[i].copy()
        dummy[i][0] = deleteStopWord(dummy[i][0], listOfStopWord)
    query = removeStopRegex(query, listOfStopWord)
    query = query.replace(" ", ".*")
    length = len(query)
    i = 0
    startIdx = -1
    endIdx = -1
    while (i < len(query)):
        if (query[i].isalpha()):
            if (startIdx == -1):
                startIdx = i
            elif (i == len(query)-1):
                endIdx = i+1
                res = regexAddSynonim(i, startIdx, endIdx, query, query[startIdx:endIdx])
                query = res['query']
                i = res['idx']
                startIdx = -1
        elif (startIdx != -1) :
            endIdx = i
            res = regexAddSynonim(i, startIdx, endIdx, query, query[startIdx:endIdx])
            query = res['query']
            i = res['idx']
            startIdx = -1
        i += 1
    idxMatchedQuestion = []
    for i in range (len(dummy)):
        x = re.search(query, dummy[i][0], flags = re.IGNORECASE)
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
