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

def deleteStopWord(pattern, listOfStopWord):
#clean the received string
    for word in listOfStopWord:
        x = word + " "
        pattern = pattern.replace(x, '')
        pattern = pattern.replace(word, '')
    pattern = pattern.replace('?', '')
    pattern = pattern.strip()
    return pattern

def addSynonym(pattern, listOfSynonym):
#generate list of similar string meaning with pattern
    result = [pattern]
    for word in listOfSynonym:
        temp = pattern.replace(word[0], word[1])
        if(pattern != temp):
            result.append(temp)
    return result

fStopWord = open('StopWord.txt', 'r')#readfile
listOfStopWord = [line.rstrip('\n') for line in fStopWord]

fSynonym = open('Synonym.txt', 'r')#readfile
listOfSynonym = [[word.rstrip('\n') for word in line.split(' ')] for line in fSynonym]

fQnA = open('QnA.txt', 'r')#readfile
listOfQnA = [[word.rstrip('\n').strip() for word in line.split('?')] for line in fQnA]
print(listOfQnA)

a = str(input())
a = deleteStopWord(a, listOfStopWord)
print(a)
