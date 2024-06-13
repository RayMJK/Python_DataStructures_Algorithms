n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
'''
a : [4, 1, 5, 2, 3]
b : [1, 3, 7, 9, 5]
'''

def binary_search(value, start, end):
    # print("value, start, end = ", value, start, end)
    if start > end :
        return False
    median = (start + end) // 2
    if a[median] < value:
        return binary_search(value, median+1, end)
    elif a[median] > value:
        return binary_search(value, start, median-1)
    else:
        return True
a.sort()
for num in b:
    if binary_search(num, 0, n-1):
        print(1)
    else:
        print(0)
