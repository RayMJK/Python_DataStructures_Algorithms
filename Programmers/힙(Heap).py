import heapq

def solution(jobs):
    answer = 0
    print(jobs)
    new_jobs = []
    for i in jobs:
        new_jobs.append(list(reversed(i)))
    print(new_jobs)
    heapq.heapify(new_jobs)
    duration = 0
    while len(new_jobs) > 0:
        a = heapq.heappop(new_jobs)
        duration += a[0]
        time = a[1]
        answer += duration - time
        print(answer)
    return answer//3
