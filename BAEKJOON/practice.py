
graph = dict()

n,m,v = map(int, input().split(' '))

for i in range(1, m+1):
    a, b = map(int, input().split(' '))
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

print(graph)

def DFS(graph, start_node):
    visited = []
    need_to_visit = []
    need_to_visit.append(start_node)
    while need_to_visit:
        a = need_to_visit.pop(-1)
        if a not in visited:
            visited.append(a)
            need_to_visit.extend(graph[a])
    return visited

def BFS(graph, start_node):
    visited = []
    need_to_visit=[]
    need_to_visit.append(start_node)

    while need_to_visit:
        a = need_to_visit.pop(0)
        if a not in visited:
            visited.append(a)
            need_to_visit.extend(graph[a])
    return visited




print(DFS(graph, 1))
print(BFS(graph,1))