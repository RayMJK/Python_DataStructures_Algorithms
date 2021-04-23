def solution(citations):
    citations.sort()
    n = len(citations)
    for i in range(n):
        if citations[i] >= n-i:
            # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
            return n-i
    return 0