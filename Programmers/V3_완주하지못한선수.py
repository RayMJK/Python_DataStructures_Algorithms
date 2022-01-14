import collections
def solution(participant, completion):
    answer = ''
    #print(collections.Counter(participant))
    #print(collections.Counter(completion))
    answer = collections.Counter(participant) - collections.Counter(completion)


    #print(answer)

    
    return list(answer)[0]
