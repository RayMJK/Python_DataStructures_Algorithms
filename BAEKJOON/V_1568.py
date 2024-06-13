n = int(input())
answer = 0
k = 1

while n != 0:
    if k>n :
        k = 1
    n -= k
    k+=1
    answer+=1
print(answer)