n = int(input())

'''
1 13
2 11
3 8
4 4
1 3
2 1
1 0
'''
answer = 0
check = True
while check:
    a = n
    for i in range(1, a+1):
        if a-i >= 0:
            a -= i
            answer += 1
            if a == 0:
                check = False
        else:
            n = a
            break
print(answer)

