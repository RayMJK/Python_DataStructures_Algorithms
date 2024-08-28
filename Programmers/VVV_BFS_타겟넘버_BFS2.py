from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque()
    n = len(numbers)
    q.append([numbers[0], 0])
    q.append([-1*numbers[0], 0])
    while q:
        tmp, idx = q.popleft()
        idx += 1
        if idx < n:
            q.append([tmp+numbers[idx], idx])
            q.append([tmp-numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1
    return answer