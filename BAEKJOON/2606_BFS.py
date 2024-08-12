from collections import deque

n = int(input())
k = int(input())

adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)



for i in range(k):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

# print(adj)
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

def BFS(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if visited[v] == False:
            visited[v] = True
            for e in adj[v]:
                if visited[e] == False:
                    q.append(e)
    return visited.count(True)

print(BFS(1)-1)
