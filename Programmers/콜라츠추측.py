def solution(num):
    answer = 0
    i = 0
    while i < 500 and num != 1:
        if num % 2 == 0:
            num = num // 2
            i += 1
        else:
            num = (num * 3) + 1
            i += 1
    if num != 1:
        return -1
    return i