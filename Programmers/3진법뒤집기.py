def solution(n):
    answer = 0
    result = ''
    if n == 1:
        return 1
    while (n // 3) >= 1:
        remain = n % 3
        n = n // 3
        result += str(remain)
        if n < 3 :
            result += str(n)
    for i in range(len(result)):
        if int(result[i]) == 0:
            continue
        elif int(result[i]) == 1:
            answer += ( 3**( len(result)-(i+1) ) ) * 1
        elif int(result[i]) == 2:
            answer += ( 3**( len(result)-(i+1) ) ) * 2
    return answer

print(solution(1))