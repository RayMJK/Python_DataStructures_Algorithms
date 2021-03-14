a = {'d': 1, 'b': 20, 'c': 20}


result = [k for k,v in a.items() if max(a.values()) == v]
print(result)