def solution(citations):
    answer = []
    n = len(citations)
    max_num = max(citations)
    print(max_num)
    for h in range(0, max_num + 1):
        count = 0
        for i in citations:
            if i >= h:
                count += 1
                if count == h:
                    answer.append(h)

    return max(answer)