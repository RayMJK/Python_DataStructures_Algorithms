def solution(progresses, speeds):
    answer = []
    stack = []

    for i in range(len(progresses)):
        work = 100 - progresses[i]
        day = work // speeds[i]
        if work % speeds[i] != 0:
            day += 1
        # print(day)
        if len(stack) == 0:
            stack.append(day)
        elif day <= stack[0]:
            stack.append(day)
        else:
            count = len(stack)
            answer.append(count)
            stack.clear()
            stack.append(day)
    if len(stack) != 0:
        answer.append(len(stack))
    return answer