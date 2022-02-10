from itertools import combinations
def solution(number, k):
    
    answer = ''
    numlist = list(number)      # ['1', '9', '2', '4']
    #print(numlist)
    
    new = list(combinations(numlist, len(numlist)-k) )
    #print(new)
    new.sort(reverse= True)
    #print(new)
    
    answer_list = list(new[0])
    #print(answer_list)
    for i in answer_list:
        answer += i
    return answer
