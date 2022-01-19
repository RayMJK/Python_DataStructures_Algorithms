def solution(priorities):
    answer = 0
    stack = []
    result = []
    maximum = max(priorities)
    for pri, i in zip(priorities, range(len(priorities))):
        stack.append((pri, i))
    print(stack)

    while len(stack) != 0:
        for j in stack:
            maximum = max(stack, key=lambda x:x[0])
            print(j[0], maximum[0])

            if j[0] >= maximum[0]:
                b = stack.pop(0)
                result.append(b)
            else:  # j[0] < maximum
                b = stack.pop(0)
                stack.append(b)
    print(result)
    return answer

print(solution(([2, 1, 3, 2])))