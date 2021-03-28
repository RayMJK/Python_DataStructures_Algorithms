def solution(n):
    answer = 0
    str_n = str(n)
    nlist = []
    for i in str_n:
        nlist.append(i)
    nlist.sort()
    nlist.reverse()
    result = ''.join(nlist)
    answer = int(result)
    return answer

print(solution(118372))