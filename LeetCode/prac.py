from itertools import combinations

a = []
b = []
items= [1,2,3,4]
for i in list(combinations(items,2)):
    a.append(i)
print(a)

