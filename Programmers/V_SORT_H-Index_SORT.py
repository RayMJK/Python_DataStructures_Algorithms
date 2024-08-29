def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    # print(citations)
    # [6, 5, 3, 1, 0]
    for i in range(len(citations)):
        if i >= citations[i]:
            answer = i
            return answer
    return len(citations)