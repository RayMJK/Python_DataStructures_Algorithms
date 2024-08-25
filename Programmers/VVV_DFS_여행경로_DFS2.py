def solution(tickets):
    answer = []

    visited = [False for _ in range(len(tickets))]

    def dfs(airport, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return

        for idx, ticket in enumerate(tickets):
            if airport != ticket[0] or visited[idx] == True:
                continue
            visited[idx] = True
            dfs(ticket[1], path + [ticket[1]])
            visited[idx] = False

    dfs("ICN", ["ICN"])
    answer.sort()

    return answer[0]