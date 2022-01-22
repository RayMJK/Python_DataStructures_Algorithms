import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        answer += 1
        scov = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, scov)

        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer