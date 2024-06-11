
n = int(input())
array= []
'''
5
25 3 4
4 4 6
9 2 3
16 2 5
1 5 2
'''

array.append((0, 0, 0, 0))

for i in range(1, n+1):
    area, height, weight = map(int, input().split())
    array.append((i, area, height, weight))

#print(array)
'''
[
(0, 0, 0, 0), 
(1, 25, 3, 4), 
(2, 4, 4, 6), 
(3, 9, 2, 3), 
(4, 16, 2, 5), 
(5, 1, 5, 2)
]
'''
array.sort(key=lambda data:data[3])
#print(array)


'''
[
(0, 0, 0, 0), 
(5, 1, 5, 2), 
(3, 9, 2, 3), 
(1, 25, 3, 4), 
(4, 16, 2, 5), 
(2, 4, 4, 6)
]
'''
dp = [0] * (n+1)
# [0, 0, 0, 0, 0, 0]
for i in range(1, n+1):
    for j in range(0, i):
        if array[i][1] > array[j][1]:
            dp[i] = max(dp[i], dp[j] + array[i][2])
# print(dp)
# [0, 5, 7, 10, 9, 9]
max_value = max(dp)
# print(max_value)
index = n
result = []

while index != 0:
    if max_value == dp[index]:
        result.append(array[index][0])
        max_value -= array[index][2]
    index -= 1

result.reverse()
print(len(result))
[print(i) for i in result]