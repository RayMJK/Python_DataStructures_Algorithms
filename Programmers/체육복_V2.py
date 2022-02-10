def solution(n, lost, reserve):
    answer = []
    for a in reserve:
        if a in lost:
            reserve.remove(a)
            lost.remove(a)
    for i in range(1, n+1):
        if i in reserve:
            if i in lost:
                reserve.remove(i)
            answer.append(i)
        else:
            if i in lost:
                if i-1 in reserve:
                    reserve.remove(i-1)
                    answer.append(i)
                elif i+1 in reserve:
                    reserve.remove(i+1)
                    answer.append(i)
            else:
                answer.append(i)
                
    return len(answer)
