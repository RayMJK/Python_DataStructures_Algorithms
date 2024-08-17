N, K = map(int, input().split())
M = [list(input()) for _ in range(N)]
ck = [[False for i in range(10)] for _ in range(N)]
ck2 = [[False for i in range(10)] for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def dfs(x, y):
    ck[x][y] = True
    count = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if ck[xx][yy] or M[x][y] != M[xx][yy]:
            continue
        count += dfs(xx, yy)
    return count

def dfs2(x, y, m):
    ck2[x][y] = True
    M[x][y] = '0'
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if ck2[xx][yy] or M[xx][yy] != m:
            continue
        dfs2(xx, yy, m)

def down():
    for i in range(10):
        lst = []
        for j in range(N):
            if M[j][i] != '0':
                lst.append(M[j][i])
                M[j][i] = '0'
        for k in range(N-1, 0, -1):
            if lst:
                M[k][i] = lst.pop()

while True:
    exist = False
    ck = [[False for i in range(10)] for _ in range(N)]
    ck2 = [[False for i in range(10)] for _ in range(N)]
    for i in range(N):
        for j in range(10):
            if M[i][j] == '0' or ck[i][j]:
                continue
            count = dfs(i, j)
            if count >= K:
                dfs2(i, j, M[i][j])
                exist = True
    if not exist:
        break
    down()

for i in M:
    print(''.join(i))