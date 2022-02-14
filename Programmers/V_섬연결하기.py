def solution(n, costs):
    answer = 0
    # print(costs)
    costs.sort(key=lambda x: x[2])
    #print(costs)
    connect = set([costs[0][0]])
    #print('connect =', connect)

    while len(connect) != n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:
                continue

            if cost[0] in connect or costs[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer
