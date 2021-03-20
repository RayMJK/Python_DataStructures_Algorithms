inp_str = "aaaaZZZZ)"
count_dict = dict()
for i in inp_str:
    if count_dict.get(i) == None:
        count_dict[i] = 1
    else:
        count_dict[i] += 1
max = -1
for key in count_dict:
    if count_dict[key] > max:
        max = count_dict[key]

print(max)