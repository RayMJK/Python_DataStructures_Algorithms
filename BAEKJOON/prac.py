n, k = map(int, input().split())
m = [list(input()) for _ in range(n)]
ck = [[False] * 10 for _ in range(n)]
ck2 = [[False] * 10 for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]


def dfs(x, y):
    ck[x][y] = True
    count = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= n or yy < 0 or yy >= 10:
            continue
        if ck[xx][yy] or m[x][y] != m[xx][yy]:
            continue
        count += dfs(xx, yy)
    return count


def dfs2(x, y, value):
    ck2[x][y] = True
    m[x][y] = '0'
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= n or yy < 0 or yy >= 10:
            continue
        if ck2[xx][yy] == True or m[xx][yy] != value:
            continue
        dfs2(xx, yy, value)

def down():
    for i in range(10):
        lst = []
        for j in range(n):
            if m[j][i] != '0':
                lst.append(m[j][i])
                m[j][i] = '0'
        for k in range(n-1, 0, -1):
            if lst:
                m[k][i] = lst.pop()


while True:
    exist = False
    ck = [[False for i in range(10)] for _ in range(n)]
    ck2 = [[False for i in range(10)] for _ in range(n)]
    for i in range(n):
        for j in range(10):
            if m[i][j] == '0' or ck[i][j]:
                continue
            count = dfs(i, j)
            if count >= k:
                dfs2(i, j, m[i][j])
                exist = True
    if not exist:
        break
    down()

for i in m:
    print(''.join(i))

'''
print(array)
[
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], 
    ['0', '0', '0', '0', '0', '0', '0', '3', '0', '0'], 
    ['0', '0', '5', '4', '0', '0', '0', '3', '0', '0'], 
    ['1', '0', '5', '4', '5', '0', '2', '2', '3', '0'], 
    ['2', '2', '1', '1', '1', '2', '2', '2', '2', '0'], 
    ['1', '1', '1', '1', '1', '1', '1', '2', '2', '3']
]
'''
