from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[y].append(x)

# print(adj)
# [[], [3], [3], [4, 5], [], []]

def BFS(v):
    q = deque([v])
    visited = [False] * (n+1)
    visited[v] = True
    count = 1
    while q:
        v = q.popleft()
        for e in adj[v]:
            if visited[e] == False:
                q.append(e)
                visited[e] = True
                count += 1
    return count

result = []
max_value = -1

for i in range(1, n+1):
    c = BFS(i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c
for e in result:
    print(e, end=' ')
