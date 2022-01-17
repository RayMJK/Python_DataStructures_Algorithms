import collections
def solution(participant, completion):
    answer = ''
    #print(collections.Counter(participant))
    #print(collections.Counter(completion))
    
    answer = collections.Counter(participant) - collections.Counter(completion)
    #print(answer)
    #print(list(answer)[0])
    return list(answer)[0]
