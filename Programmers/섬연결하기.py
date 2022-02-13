def solution(n, costs):
    answer = 0
    stack = []
    for i in range(n):
        cost = dict()
        for j in range(len(costs)):
            if i == costs[j][0]:
                stack.append(i)
                cost[costs[j][1]] = costs[j][2]
        min_val = min(cost.values())
        min_key = min(cost, key=cost.get)
        stack.append(min_key)
        answer += min_val
    stack = list(set(stack))
    print(stack)
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	))