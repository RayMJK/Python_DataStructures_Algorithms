def solution(participant, completion):
    answer = ''
    hashDict = {}
    sumHash = 0
    
    for i in participant:
        hashDict[hash(i)] = i
        sumHash += hash(i)
    #print(hashDict)
    
    for c in completion:
        sumHash -= hash(c)
    
    return hashDict[sumHash]
