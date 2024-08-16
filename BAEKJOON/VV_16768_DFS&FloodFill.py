import sys
sys.setrecursionlimit(1000000)

n, k = map(int,input().split())
m = [[]*10 for _ in range(n)]
visited = [[False]*10 for _ in range(n)]
visited2 = [[False]*10 for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0,-1,0,1]

for i in range(n):
    a = list(map(int, input()))
    m[i] = a

'''
    [    
         0  1  2  3  4  5  6  7  8  9 

0       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
1       [0, 0, 0, 0, 0, 0, 0, 3, 0, 0], 
2       [0, 0, 5, 4, 0, 0, 0, 3, 0, 0], 
3       [1, 0, 5, 4, 5, 0, 2, 2, 3, 0], 
4       [2, 2, 1, 1, 1, 2, 2, 2, 2, 0], 
5       [1, 1, 1, 1, 1, 1, 1, 2, 2, 3]
    
    ]
'''
def DFS(x,y):
    visited[x][y] = True
    count = 1
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=10:
            continue
        if visited[nx][ny] == True or m[nx][ny] != m[x][y]:
            continue
        count += DFS(nx, ny)
    return count

def DFS2(x,y,z):
    visited2[x][y] = True
    m[x][y] = 0
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=10:
            continue
        if visited2[nx][ny] == True or m[nx][ny] != z:
            continue
        DFS2(nx, ny, z)

def down():
    for i in range(10):
        lst = []
        for j in range(n):
            if m[j][i] != 0:
                lst.append(m[j][i])
                m[j][i] = 0
        for w in range(n-1, 0, -1):
            if len(lst) != 0:
                m[w][i] = lst.pop()




while True:
    exist = False
    visited = [[False]*10 for _ in range(n)]
    visited2 = [[False]*10 for _ in range(n)]
    for i in range(n):
        for j in range(10):
            if m[i][j] == 0 or visited[i][j] == True:
                continue
            count = DFS(i,j)
            if count >= k:
                DFS2(i,j, m[i][j])
                exist = True
    if exist == False:
        break
    down()

for i in m:
    for j in i:
        print(j,end="")
    print(end='\n')
'''
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 3, 0, 0], 
        [0, 0, 5, 4, 0, 0, 0, 3, 0, 0], 
        [1, 0, 5, 4, 5, 0, 0, 0, 3, 0], 
        [2, 2, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 3]
    ]
'''
