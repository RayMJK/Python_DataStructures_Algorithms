from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [False for _ in range(len(words))]
    q = deque()
    q.append([begin, 0])

    while q:
        now_word, step = q.popleft()
        if now_word == target:
            answer = step
            break
        for i in range(len(words)):
            tmp_cnt = 0
            if visited[i] == False:
                for j in range(len(now_word)):
                    if now_word[j] != words[i][j]:
                        tmp_cnt += 1
                if tmp_cnt == 1:
                    q.append([words[i], step+1])
                    visited[i] = True

    return answer