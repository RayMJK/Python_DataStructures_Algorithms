def solution(strings, n):

    answer = []
    result = dict()
    for i in strings:
        result[i] = i[n]
    result = sorted(result.items(), key=lambda x:x[1])
    result = sorted(result, key = lambda x : (x[1], x[0]))
    for i in result:
        answer.append(i[0])
    return answer
strings = ["abce", "abcd", "cdx"]
n = 2
print(solution(strings, n))