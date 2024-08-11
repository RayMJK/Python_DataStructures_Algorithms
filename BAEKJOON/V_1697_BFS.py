from collections import deque
max_value = 100001
n, k = map(int, input().split())

array = [0] * max_value

def BFS():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return array[now_pos]
        
        for next_pos in (now_pos-1, now_pos+1, 2*now_pos):
            if 0 <= next_pos < max_value and array[next_pos] == 0:
                array[next_pos] = array[now_pos] + 1
                q.append(next_pos)

print(BFS())

