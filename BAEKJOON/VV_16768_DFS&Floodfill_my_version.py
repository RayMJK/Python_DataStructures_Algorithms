n, k = map(int, input().split())
m = [list(map(int, input())) for _ in range(n)]
ck = [[False] * 10 for _ in range(n)]
ck2 = [[False] * 10 for _ in range(n)]
'''
print(m)
[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 3, 0, 0], 
    [0, 0, 5, 4, 0, 0, 0, 3, 0, 0], 
    [1, 0, 5, 4, 5, 0, 2, 2, 3, 0], 
    [2, 2, 1, 1, 1, 2, 2, 2, 2, 0], 
    [1, 1, 1, 1, 1, 1, 1, 2, 2, 3]
]

'''
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def dfs(x, y):
    ck[x][y] = True
    count = 1
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= 10:
            continue
        if ck[nx][ny] == True or m[nx][ny] != m[x][y]:
            continue
        count += dfs(nx,ny)
    return count

def dfs2(x, y, value):
    ck2[x][y] = True
    m[x][y] = 0
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= 10:
            continue
        if ck2[nx][ny] == True or m[nx][ny] != value:
            continue
        dfs2(nx,ny,value)

def down():
    for j in range(10):
        tmp = []
        for i in range(n):
            if m[i][j] != 0 :
                tmp.append(m[i][j])
                m[i][j] = 0
        for k in range(n-1, -1, -1):
            if len(tmp) > 0:
                m[k][j] = tmp.pop()

while True:
    exist = False
    ck = [[False] * 10 for _ in range(n)]
    ck2 = [[False] * 10 for _ in range(n)]
    for i in range(n):
        for j in range(10):
            if ck[i][j] == True or m[i][j] == 0:
                continue
            count = dfs(i, j)
            if count >= k:
                dfs2(i, j, m[i][j])
                exist = True
    if exist == False:
        break
    down()


'''
print(m)
[
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[1, 0, 5, 4, 0, 0, 0, 3, 0, 0], 
[2, 2, 5, 4, 5, 0, 0, 3, 3, 3]
]
'''
for i in m:
    for j in i:
        print(j, end='')
    print(end='\n')