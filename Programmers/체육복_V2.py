def solution(n, lost, reserve):
    answer = []
    for i in range(1, n+1):
        print('i = ', i)
        if i in lost:
            if i in reserve:
                answer.append(i)
                reserve.remove(i)
                break
            else:
                if i-1 in reserve:
                    answer.append(i)
                    reserve.remove(i-1)
                    print('ssibal=',answer)
                    break
                elif i+1 in reserve:
                    answer.append(i)
                    reserve.remove(i+1)
        else:
            answer.append(i)
            print('sssibal =', answer)
        print('reserve =', reserve)
        print('answer =', answer)
    #print(answer)
    return len(list(set(answer)))

print(solution(5, [2,4], [1,3,5]))
