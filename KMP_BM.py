from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from tesaurus import *
import re

def removeStopWord(kalimat):
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    stop = stopword.remove(kalimat)
    return stop

def KMP(pattern, text):
#String Matching versi 1
    n = len(text)
    m = len(pattern)

    fail = checkFail(pattern)
    temp = 0
    max = 0
    i = 0
    j = 0
    if(n<m):
        return 0.0
    while (i<n):
        if(pattern[j] == text[i]):
            temp += 1
            if (j == m - 1):
                return m*100/n
            i += 1
            j += 1
        elif (j>0):
            temp = 0
            j = fail[j-1]
        else:
            temp = 0
            i += 1
        if(max < temp):
            max = temp
    return max*100/n

def checkFail(pattern):
#Utility function for KMP
    fail = []
    fail.append(0)
    m = len(pattern)
    i = 1
    j = 0
    while(i<m):
        if(pattern[j] == pattern[i]):
            fail.append(j+1)
            i += 1
            j += 1
        elif(j>0):
            j = fail[j-1]
        else:
            fail.append(0)
            i += 1
    return fail

def BM(pattern, text):
    last = makeLast(pattern)
    n = len(text)
    m = len(pattern)
    i = m-1
    if(n<m):
        return 0.0
    j = m-1
    
    if(pattern[j] == text[i]):
        if(j == 0):
            return m*100/n
        else :
            i -= 1
            j -= 1
    else:
        lastOcc = last[ord(text[i])]
        if(j < 1+lastOcc):
            i += m - j
        else:
            i += m- lastOcc
        j = m-1

    while (i<=n-1):
        if(pattern[j] == text[i]):
            if(j == 0):
                return m*100/n
            else :
                i -= 1
                j -= 1
        else:
            lastOcc = last[ord(text[i])]
            if(j < 1+lastOcc):
                i += m - j
            else:
                i += m- lastOcc
            j = m-1
    return 0.0

def makeLast(pattern):
    last = [-1 for i in range(128)]
    m = len(pattern)
    for i in range(m):
        last[ord(pattern[i])] = i
    return last

def addSynonym(pattern, listOfSynonym):
#generate list of similar string meaning with pattern
    result = [pattern]
    for word in listOfSynonym:
        temp = pattern.replace(word[0], word[1])
        if(pattern != temp):
            result.append(temp)
    return result

def deleteStopWord(pattern, listOfStopWord):
#clean the received string
    for word in listOfStopWord:
        x = word + " "
        pattern = pattern.replace(x, '')
        pattern = pattern.replace(word, '')
    pattern = pattern.replace('?', '')
    pattern = pattern.strip()
    return pattern

def solveQuery(pattern):
    fStopWord = open('StopWord.txt', 'r')#readfile
    listOfStopWord = [line.rstrip('\n') for line in fStopWord]
    dummy = [None for i in range(len(listOfQnA))]
    for i in range(len(listOfQnA)):
        dummy[i]=listOfQnA[i].copy()
    pattern=pattern.lower()
    pattern = deleteStopWord(pattern, listOfStopWord)
    modified_pattern = [pattern]
    words = pattern.split(' ')
    for i in words:
        sinonim = getSinonim(i)
        for j in sinonim:
            modified_pattern.append(pattern.replace(i, j))
    max = [0 for i in range(3)]
    indexQnA = [0 for i in range(3)]
    index = 0
    for question in dummy:
        question[0] = question[0].lower()
        question[0] = deleteStopWord(question[0], listOfStopWord)
        for x in modified_pattern:
            score = KMP(x, question[0])
            score2 = KMP(question[0], x)
            if(score < score2):
                score = score2
            if(score >= max[0]):
                max[0] = score
                indexQnA[0] = index
            elif(score >= max[1] and question[0] != dummy[indexQnA[0]][0]):
                max[1] = score
                indexQnA[1] = index
            elif(score >= max[2] and question[0] != dummy[indexQnA[1]][0] and question[0] != dummy[indexQnA[0]][0]):
                max[2] = score
                indexQnA[2] = index
        index += 1
    
    if(max[0] != 100):
        index = 0
        for question in dummy:
            question[0] = removeStopWord(question[0])
            for x in modified_pattern:
                score = specialCase(x, question[0])
                score2 = specialCase(question[0], x)
                if(score < score2):
                    score = score2
                if(score >= max[0]):
                    max[0] = score
                    indexQnA[0] = index
                elif(score >= max[1] and question[0] != dummy[indexQnA[0]][0]):
                    max[1] = score
                    indexQnA[1] = index
                elif(score >= max[2] and question[0] != dummy[indexQnA[1]][0] and question[0] != dummy[indexQnA[0]][0]):
                    max[2] = score
                    indexQnA[2] = index
            index += 1
    if(max[0] >= 90 and max[1] < 90):
        print(listOfQnA[indexQnA[0]][1])
    elif(max[0] >= 90 and max[1] >= 90 and max[2] < 90):
        print('- '+listOfQnA[indexQnA[0]][0]+'?')
        print('- '+listOfQnA[indexQnA[1]][0]+'?')
    else:
        print('- '+listOfQnA[indexQnA[0]][0]+'?')
        print('- '+listOfQnA[indexQnA[1]][0]+'?')
        print('- '+listOfQnA[indexQnA[2]][0]+'?')
    print(max[0])

def specialCase(pattern, text):
    #comparing each word
    if(len(pattern) <= len(text)):
        words = pattern.split()
        words2 = text.split()
        point = 0
        for i in words:
            max = 0
            count = 0
            for j in words2:
                score = BM(i,j)
                score2 = BM(j,i)
                if(score < score2):
                    score = score2
                if(score > max):
                    max = score  
                count += len(j)
            point += len(i)*max
        return point/count
    else:
        return 0.0

fQnA = open('QnA.txt', 'r')#readfile
listOfQnA = [[word.rstrip('\n').strip() for word in line.split('?')] for line in fQnA]
