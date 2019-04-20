from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from tesaurus import *
import re

def controller(query):
    splitBySpace = query.split(" ")
    isRegex = False
    i = 0
    while (i < len(splitBySpace) and not isRegex):
        isRegex = not splitBySpace[i].isalnum()
        i += 1
    if (isRegex):
        Regex(query)
    else:
        #do something
        pass

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
            # print( regexAddSynonim(i, startIdx, endIdx, query, query[startIdx:(endIdx+1)]))
            res = regexAddSynonim(i, startIdx, endIdx, query, query[startIdx:endIdx])
            query = res['query']
            i = res['idx']
            print(i)
            startIdx = -1
        i += 1
    print(query)
    idxMatchedQuestion = []
    for i in range (len(listOfQnA)):
        x = re.search(query, listOfQnA[i][0], flags = re.IGNORECASE)
        if (x != None):
            idxMatchedQuestion.append(i)
    for i in range (len(idxMatchedQuestion)):
        print(listOfQnA[idxMatchedQuestion[i]][0])

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
        lastOcc = last[text[i]]
        i += m
        j = m-1

    while (i<=n-1):
        if(pattern[j] == text[i]):
            if(j == 0):
                return m*100/n
            else :
                i -= 1
                j -= 1
        else:
            lastOcc = last[i]
            i += m
            j = m-1
    return 0.0

def makeLast(pattern):
    last = [-1 for i in range(128)]
    m = len(pattern)
    for i in range(m):
        last[i] += i
    return last

def addSynonym(pattern, listOfSynonym):
#generate list of similar string meaning with pattern
    result = [pattern]
    for word in listOfSynonym:
        temp = pattern.replace(word[0], word[1])
        if(pattern != temp):
            result.append(temp)
    return result

def solveQuery(pattern):
    pattern = removeStopWord(pattern)
    modified_pattern = [pattern]
    words = pattern.split()
    for i in words:
        modified_pattern.append(pattern.replace(i, getSinonim(i)))
    print(modified_pattern)
    max = [0 for i in range(3)]
    temp = [["None", "None"] for i in range(3)]
    for question in listOfQnA:
        for x in modified_pattern:
            score = KMP(x, question[0])
            score2 = KMP(question[0], x)
            if(score < score2):
                score = score2
            if(score >= max[0] and question != temp[0] and question != temp[1] and  question != temp[2]):
                max[0] = score
                temp[0] = question
            elif(score >= max[1] and question != temp[0] and question != temp[1] and  question != temp[2]):
                max[1] = score
                temp[1] = question
            elif(score >= max[2] and question != temp[0] and question != temp[1] and  question != temp[2]):
                max[2] = score
                temp[2] = question
    print(max)
    if(max[0] >= 90):
        print(temp[0][1])
    else:
        print(temp[0][1])
        print(temp[1][1])
        print(temp[2][1])

def specialCase(pattern, text):
    #comparing each word
    words = pattern.split()
    words2 = text.split()
    point = 0
    count = 0
    for i in words:
        max = 0
        for j in words2:
            score = KMP(i,j)
            score2 = KMP(j,i)
            if(score < score2):
                score = score2
            if(score > max):
                max = score
        point += len(i)*max
        count += len(i)
    return point/count

# fStopWord = open('StopWord.txt', 'r')#readfile
# listOfStopWord = [line.rstrip('\n') for line in fStopWord]

# fSynonym = open('Synonym.txt', 'r')#readfile
# listOfSynonym = [[word.rstrip('\n') for word in line.split(' ')] for line in fSynonym]

fQnA = open('QnA.txt', 'r')#readfile
listOfQnA = [[word.rstrip('\n').strip() for word in line.split('?')] for line in fQnA]
# print(listOfQnA)

# a = str(input())
# b = str(input())
# c = specialCase(a, b)
# print(c)
# listOfAnswer = solveQuery(a, listOfStopWord, listOfQnA, listOfSynonym)
# print(listOfAnswer)

# === Remove Stop Word ===
# kalimat = 'Dengan Menggunakan Python dan Library Sastrawi saya dapat melakukan proses Stopword Removal'
# print(removeStopWord(kalimat))

# === Find Synonym ===
# print(getSinonim('Spain'))

# === Regex ===
# # txt = 'the rain in spain'
# x = re.search('^siapa*', 'abc', flags = re.IGNORECASE)
# print(x)
Regex('^siapa nama.*')

# regexAddSynonim(0,5,8,'saya suka kamu', 'suka')
txt = 'burung'