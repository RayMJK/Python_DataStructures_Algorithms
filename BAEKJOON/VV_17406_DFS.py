from copy import deepcopy
'''
5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1
'''

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
q = [tuple(map(int, input().split())) for _ in range(k)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
'''
print(a)
[
    [1, 2, 3, 2, 5, 6], 
    [3, 8, 7, 2, 1, 3], 
    [8, 2, 3, 1, 4, 5], 
    [3, 4, 5, 1, 1, 1], 
    [9, 3, 2, 1, 4, 3]
]
'''
ans = 100000

def value(arr):
    return min([sum(i) for i in arr])

def convert(arr, qry):
    (r,c,s) = qry
    r, c = r-1, c-1
    new_arr = deepcopy(arr)
    for i in range(1, s+1):
        rr, cc = r-i, c+i
        for w in range(4):
            for d in range(i*2):
                rrr, ccc = rr + dx[w], cc + dy[w],
                new_arr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc
    return new_arr

def dfs(arr, qry):
    global ans
    if sum(qry) == k:
        ans = min(ans, value(arr))
        return
    for i in range(k):
        if qry[i]:
            continue
        new_arr = convert(arr, q[i])
        qry[i] = 1
        dfs(new_arr, qry)
        qry[i] = 0

dfs(a, [0 for i in range(k)])
# print(ans)
'''
print(convert(a, (3,4,2)))
[
    [1, 8, 2, 3, 2, 5], 
    [3, 2, 3, 7, 2, 6], 
    [8, 4, 5, 1, 1, 3], 
    [3, 3, 1, 1, 4, 5], 
    [9, 2, 1, 4, 3, 1]
]
'''