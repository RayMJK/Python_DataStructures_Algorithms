from collections import deque

n, m, v = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

# print(adj)
# [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

for i in adj:
    i.sort()
# print(adj)
# [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]


def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for e in adj[v]:
        if visited[e] == False:
            dfs(e)


def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        visited[v] = True
        print(v, end=' ')
        for e in adj[v]:
            if visited[e] == False:
                visited[e] = True
                q.append(e)


visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
