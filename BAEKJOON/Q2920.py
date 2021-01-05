a = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(1,len(a)):
    if a[i] > a[i-1]:
        descending = False
    elif a[i] < a[i-1]:
        ascending = False

if ascending:
    print('asending')
elif descending:
    print('descending')
else:
    print('mixed')