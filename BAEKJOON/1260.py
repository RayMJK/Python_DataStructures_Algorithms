
graph = dict()

n, m, v = map(int, input().split(' '))
'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''
for i in range(1, m+ 1):
    a, b = map(int, input().split(' '))
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

# print(graph)
# {1: [2, 3, 4], 2: [1, 4], 3: [1, 4], 4: [1, 2, 3]}
# print(graph[1]) : [2, 3, 4]

reversed_graph = {key : sorted(value, reverse=True) for key, value in graph.items()}
print(reversed_graph)
graph = {key : sorted(value) for key, value in graph.items()}

def DFS(graph, start_node):
    visted = []
    need_to_visit = []
    need_to_visit.append(start_node)

    while need_to_visit:
        a = need_to_visit.pop()
        if a not in visted:
            visted.append(a)
            need_to_visit.extend(graph[a])
    return visted

def BFS(graph, start_node):
    visted = []
    need_to_visit = []
    need_to_visit.append(start_node)

    while need_to_visit:
        a = need_to_visit.pop(0)
        if a not in visted:
            visted.append(a)
            need_to_visit.extend(graph[a])

    return visted

print(*DFS(reversed_graph, v))
print(*BFS(graph, v))
