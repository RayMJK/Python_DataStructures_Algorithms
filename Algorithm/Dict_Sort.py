score_dict = {
    'A':23,
    'C':30,
    'B':29,
    'F':27,
    'E':31,
    'K':28
}
sort_dict = sorted(score_dict.keys(), reverse=True)
print(sort_dict)
sort_dict = sorted(score_dict.values(), reverse=True)
print(sort_dict)
sort_dict = sorted(score_dict.items(), key=lambda x: x[1])
print(sort_dict)
sort_dict = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)
print(sort_dict)
