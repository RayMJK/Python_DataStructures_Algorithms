def solution(numbers):
    answer = 0
    case = []
    num = ''
    for i in range(len(numbers)):
        num += numbers[i]
        case.append(int(num))


    print(case)

    return answer

print(solution("17"))

print(solution("011"))