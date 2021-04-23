a =[3, 30, 34, 5, 9]

a = list(map(str, a))
print(a)

a.sort(key= lambda x : x*3, reverse = True)
print(a)

print(str(int(''.join(a))))
