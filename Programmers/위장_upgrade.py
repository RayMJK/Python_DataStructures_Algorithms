def solution(clothes):
    answer = 0
    new = {}
    for i in clothes:
        if i[1] not in new:
            new[i[1]] = 1
        else:
            new[i[1]] += 1
    count = 1
    #print(new)
    for i in new.values():
        count *= (i+1)
    answer = count - 1
    return answer