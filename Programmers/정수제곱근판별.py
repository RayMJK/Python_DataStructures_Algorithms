def solution(n):
    answer = 0
    root_num = n**0.5
    if root_num == int(root_num):
        answer = (root_num+1)**2
    else:
        return -1
    return answer
