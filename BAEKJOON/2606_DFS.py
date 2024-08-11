n = int(input())
c = int(input())

adj = [[] for _ in range(n+1)]
for _ in range(c):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# print(adj)
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

visited = [False]*(n+1)
# [False, False, False, False, False, False, False, False]
answer = 0
def dfs(v):
    global answer
    visited[v] = True
    for i in adj[v]:
        if visited[i] == False:
            answer += 1
            dfs(i)
    return answer

print(dfs(1))