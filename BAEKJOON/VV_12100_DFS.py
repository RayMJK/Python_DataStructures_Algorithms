from copy import deepcopy
'''
3
2 2 2
4 4 4
8 8 8
'''
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
'''
print(b)
[
    [2, 2, 2], 
    [4, 4, 4], 
    [8, 8, 8]
]
'''

def rotate(b, n):
    nb = deepcopy(b)
    for i in range(n):
        for j in range(n):
            nb[n-j-1][i] = b[i][j]
    return nb

def move_left(lst):
    new_list = [i for i in lst if i]
    for i in range(len(new_list)-1):
        if new_list[i] == new_list[i+1]:
            new_list[i] *= 2
            new_list[i+1] = 0
    new_list = [i for i in new_list if i]
    return new_list + [0]*(len(lst)-len(new_list))

def dfs(b, count, n):
    result = max([max(i) for i in b])
    if count == 0:
        return result

    for _ in range(4):
        x = [move_left(i) for i in b]
        if b != x:
            result = max(result, dfs(x, count-1, n))
        b = rotate(b, n)
    return result

print(dfs(board, 5, n))