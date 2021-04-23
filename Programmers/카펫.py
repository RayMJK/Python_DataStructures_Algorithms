def solution(brown, yellow):
    answer = []
    # print(brown, yellow)
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            width = i
            length = yellow // i
            # print(width, length)

        if 2 * (length + 2) + width * 2 == brown:
            print(width, length)
            answer.append(width + 2)
            answer.append(length + 2)

    if len(list(set(answer))) == 1:
        return answer
    answer = list(set(answer))
    answer.sort()
    answer.reverse()
    return answer