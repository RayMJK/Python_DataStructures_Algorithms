N, M = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))

n_sum = 0
sum_max = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_val = numbers[i]+numbers[j]+numbers[k]
            if sum_val <= M:
                sum_max = max(sum_max, sum_val)
print(sum_max)
print('aaa')

