def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count_first = 0
    count_second = 0
    count_third = 0
    for i in range(len(answers)):
        if answers[i] == first[i]:
            count_first += 1

        if answers[i] == first[i]:
            count_second += 1

        if answers[i] == first[i]:
            count_third += 1

    answer.append(count_first)
    answer.append(count_first)
    answer.append(count_first)
    max_score = max(answer)
    max_index = answer.index(max_score)

    return max_index

print(solution())