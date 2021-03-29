def solution(arr):
    answer = []
    if len(arr)==1:
        answer.append(-1)
        return answer
    mini = min(arr)
    arr.remove(mini)
    return arr