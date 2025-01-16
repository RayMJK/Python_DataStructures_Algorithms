from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1] * 102 for _ in range(102)]
    visited = [[False] * 102 for _ in range(102)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = deque()

    for r in rectangle:
        x1, y1, x2, y2 = 2 * r[0], 2 * r[1], 2 * r[2], 2 * r[3]
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1

    cx, cy, ix, iy = 2 * characterX, 2 * characterY, 2 * itemX, 2 * itemY

    q.append((cx, cy, 0))
    visited[cx][cy] = True
    while q:
        x, y, time = q.popleft()

        for dx, dy in directions:
            nx, ny, n_time = x + dx, y + dy, time + 1
            if not 0 <= nx <= 102:
                continue
            if not 0 <= ny <= 102:
                continue
            if visited[nx][ny] == True:
                continue
            if graph[nx][ny] != 1:
                continue
            q.append((nx, ny, n_time))
            visited[nx][ny] = True
            if nx == ix and ny == iy:
                return n_time // 2

    return -1