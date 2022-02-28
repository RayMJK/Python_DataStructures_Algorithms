def solution(m, n, puddles):
    answer = 0
    #print(puddles)     [[2, 2]]
    total = (m-1)*(n-1)
    p = (puddles[0][0]-1)*(puddles[0][1]-1)+1
    answer = total - p
    return answer