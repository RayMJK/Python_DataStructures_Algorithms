def solution(tickets):
    answer = []
    # 1. 그래프 생성
    way = dict()
    
    # 2. 시작점 - [끝점] 역순으로 정렬
    for (start, end) in tickets:
        if way.get(start) is None:
            way[start] = [end]
        else:
            way[start] += [end]
    
    for start in way.keys():
        way[start].sort(reverse=True)
    
    # 3. DFS 알고리즘으로 path를 만들어줌.
    stack = ["ICN"]
    path = []
    
    while stack:
        top = stack[-1]
        if top not in way or len(way[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(way[top][-1])
            way[top] = way[top][:-1]
    
    # 4. 만든 path를 거꾸로 돌림.
    answer = path[::-1]
    return answer
