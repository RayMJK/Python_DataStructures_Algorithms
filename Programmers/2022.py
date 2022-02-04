def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count_first = 0
    count_second = 0
    count_third = 0
    result = []
    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            count_first += 1

        if answers[i] == second[i % len(second)]:
            count_second += 1

        if answers[i] == third[i % len(third)]:
            count_third += 1

    answer.append(count_first)
    answer.append(count_second)
    answer.append(count_third)
    # print('answer =', answer)
    max_score = max(answer)
    for person, score in enumerate(answer):
        if score == max_score:
            result.append(person + 1)

    return result