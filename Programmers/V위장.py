from itertools import combinations

def solution(clothes):
    answer = 0
    case = {}
    a = 1
    clotes = sorted(clothes, key=lambda x: x[1])

    for i in range(len(clothes)):
        if clothes[i][1] in case:
            case[clothes[i][1]] += 1
        else:
            case[clothes[i][1]] = 1

    count = list(case.values())
    print(count)
    for value in count:
        answer += value
    if len(count) == 1:
        return answer
    else:
        for i in range(2, len(count) + 1):
            c = list(combinations(count, i))

            for j in range(len(c)):
                mul = 1
                for k in range(len(c[j])):
                    mul *= c[j][k]
                    answer += mul
    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print()
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))