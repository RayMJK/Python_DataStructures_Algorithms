def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer: 
            answer[i[1]] += 1
        else: answer[i[1]] = 1
    print(answer)
    count = 1
    for i in answer.values():
        print(i)
        count *= (i+1)

    return count - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))