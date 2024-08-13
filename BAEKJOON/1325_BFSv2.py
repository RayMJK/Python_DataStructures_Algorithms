from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    result = 0
    q = deque([v])
    visited = [False] * (n + 1)
    while q:
        v = q.popleft()
        if visited[v] == False:
            visited[v] = True
            result += 1
            for e in adj[v]:
                if visited[e] == False:
                    q.append(e)
    return result

n,m = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    adj[b].append(a)

visited = [False]*(n+1)
# visited : [False, False, False, False, False, False]
# adj: [[], [3], [3], [4, 5], [], []]

ans_list = []

# for i in range(1,n+1):
#     visited = [False] * (n + 1)
#     ans_list.append(bfs(i))

# print(ans_llist)5 4
# 3 1
# 3 2
# 4 3
# 5 3
# [4, 4, 3, 1, 1]

# ans_list2 = []
# max_ans = max(ans_list)
# for i in range(len(ans_list)):
#     if ans_list[i] == max_ans:
#         ans_list2.append(i+1)

# print(ans_list2)
# [1, 2]

max_value = -1

for i in range(1, n+1):
    c = bfs(i)
    if c == max_value:
        ans_list.append(i)
        max_value = c
    elif c > max_value:
        ans_list = [i]
        max_value = c

print(*ans_list)

