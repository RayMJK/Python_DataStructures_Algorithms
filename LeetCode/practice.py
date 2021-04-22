a = ["119", "97674223", "1195524421"]

for i in range(len(a)):
    print(a[i])
    for j in a[i+1:] :
        if a[i] in j:
            print('false')
