def solution(seoul):
    answer = '김서방은 %d에 있다'
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            return answer %i