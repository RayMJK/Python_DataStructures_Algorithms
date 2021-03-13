import sys
result = [0,1]
for line in sys.stdin:
    if line == 0:
        answer = 0
    if line == 1:
        answer = 1
    else:
        for i in range(2, int(line)+1):
            answer = result[i-2]+result[i-1]
            result.append(answer)

    print(result[int(line)])
