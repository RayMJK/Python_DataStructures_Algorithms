import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    R, C = map(int, readl().split())
    map_jewel = [[0] + list(readl()[:-1]) + [0] if 1 <= r <= R else [0] * (C + 2) for r in range(R + 2)]
    return R, C, map_jewel

def bfs_2(x,y):
    cnt = 0
    result = False
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if not 1 <= nx <= R:
            continue
        if not 1 <= ny <= C:
            continue
        if map_jewel[nx][ny] == "L":
            cnt += 1
    if cnt == 1:
        result = True
    return result

# def bfs(r,c):
#     q = deque()
#     q.append((r,c))
#     map_jewel[r][c] = 0
#     directions = [(-1,0), (1,0), (0,-1), (0,1)]
#
#     while q:
#         x,y = q.popleft()
#         for dx, dy in directions:
#             nx, ny = x+dx, y+dy
#             if not 1<=nx<=R:
#                 continue
#             if not 1<=ny<=C:
#                 continue
#             if map_jewel[nx][ny] == "L":


def solve():
    list_a = []
    for r in range(1, R+1):
        for c in range(1, C+1):
            if map_jewel[r][c] == 'W':
                continue
            if bfs_2(r,c):
                list_a.append((r,c))
    return list_a


sol = -1
# 입력받는 부분
R, C, map_jewel = Input_Data()

# 여기서부터 작성

a = solve()
'''
print(a)
[(1, 7), (4, 1), (4, 7), (5, 2), (5, 5)]
'''

'''
print(map_jewel)
[
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 'W', 'L', 'L', 'W', 'W', 'W', 'L', 0], 
    [0, 'L', 'L', 'L', 'W', 'L', 'L', 'L', 0], 
    [0, 'L', 'W', 'L', 'W', 'L', 'W', 'W', 0], 
    [0, 'L', 'W', 'L', 'W', 'L', 'L', 'L', 0], 
    [0, 'W', 'L', 'L', 'W', 'L', 'W', 'W', 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

'''
# 출력하는 부분
print(sol)