import sys
answer = [0, 1]
for line in sys.stdin:
    if line == 0:
        print(answer[0], end="")
    if line == 1:
        print(answer[1], end="")
    else:
        for i in range(2, line+1):
            answer.append(answer[i-2]+answer[i-1])
        print(answer)
