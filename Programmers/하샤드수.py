def solution(x):
    answer = True
    n_sum = 0
    for i in str(x):
        n_sum += int(i)
    if x % n_sum != 0:
        answer = False
    return answer