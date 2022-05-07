def solution(queue1, queue2):
    answer = 0
    total = sum(queue1) + sum(queue2)
    print('total = ', total)
    target = total // 2
    print('target = ', target)

    if sum(queue1) > sum(queue2):
        a = queue1.pop(0)
        queue2.append(a)
        answer += 1
        b = queue2.pop(0)
        queue1.append(b)
        answer += 1
    else:
        a = queue2.pop(0)
        queue1.append(a)
        answer += 1
        b = queue1.pop(0)
        queue2.append(b)
        answer += 1
    # if max(queue1) == target :
    #     while queue1.pop(0) != max(queue1):
    #         a = queue1.pop(0)
    #         queue2.append(a)
    #         answer +=1
    #     a = queue1.pop(0)
    #     queue2.append(a)
    #     answer +=1
    # elif max(queue2) == target :
    #     while queue2.pop(0) != max(queue2):
    #         a = queue2.pop(0)
    #         queue1.append(a)
    #         answer +=1
    #     a = queue2.pop(0)
    #     queue1.append(a)
    #     answer +=1
    return answer