def solution(n, lost, reserve):
    answer = []
    for i in range(1, n+1):
        print(i)
        if i in lost:
            if i in reserve:
                answer.append(i)
                reserve.remove(i)
            elif i+1 in reserve:
                answer.append(i)
                reserve.remove(i+1)
            elif i-1 in reserve:
                answer.append(i)
                reserve.remove(i-1)
            
        else:
            answer.append(i)
    #print(answer) 
    return len(list(set(answer)))
