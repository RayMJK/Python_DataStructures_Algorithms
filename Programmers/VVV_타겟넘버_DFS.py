def solution(numbers, target):
    answer = 0
    stack = [[numbers[0],0], [-1*numbers[0], 0]]
    n = len(numbers)
    #print(stack)
    while stack:
        temp, idx = stack.pop()
        #print(temp, idx)
        idx += 1
        if idx < n:
            stack.append([temp+numbers[idx],idx])
            stack.append([temp-numbers[idx],idx])
            #print(stack)
        else:
            if temp == target:
                answer += 1
    return answer