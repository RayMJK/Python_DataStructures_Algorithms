def solution(n):
    answer = []
    str_n = str(n)
    for i in str_n:
        answer.append(int(i))
    answer.reverse()
    return answer