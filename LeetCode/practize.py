# Name : Myung Joon Kim (김명준)
# School : Pennsylvania State University

data = []
i = 0
while i < 10000:
    d = input()
    if d == '':
        break
    data.append(d)
    i+=1
print(data)

# the number of stars
s = 0
for i in data:
    if i == "":
        print()
        s = 0
        continue

    m = i.count("*")
    print("." * (len(i) - m - s), end="")
    print("*" * m, end="")
    print("." * s)
    s += m
