def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1
        else: answer[i[1]] = 1

    count = 1
    for i in answer.values():
        count *= (i+1)
    return count - 1