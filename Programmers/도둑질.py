def solution(money):
    answer = []
    #print(money)
    for i in range(len(money)-2):
        a = money[i]
        b = []
        for j in range(i+2, len(money)):
            b.append(money[j])
        answer.append(a+max(b))
    #print(answer)
    
    result = max(answer)
    return result