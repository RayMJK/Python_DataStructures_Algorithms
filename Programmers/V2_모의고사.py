def solution(answers):
    answer = []
    # print(answers)
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a1_count = 0
    a2_count = 0
    a3_count = 0
    result = []

    for i in range(len(answers)):
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10
        if a1[s1] == answers[i]:
            a1_count += 1
        if a2[s2] == answers[i]:
            a2_count += 1
        if a3[s3] == answers[i]:
            a3_count += 1
    result.append(a1_count)
    result.append(a2_count)
    result.append(a3_count)

    max_answer = max(a1_count, a2_count, a3_count)
    for idx, score in enumerate(result):
        if score == max_answer:
            answer.append(idx+1)
    return answer