def solution(numbers, target):
    first = [0]
    for i in numbers:
        child = []
        for j in first:
            child.append(j+i)
            child.append(j-i)
        first = child
        print(first)
    return first.count(target)