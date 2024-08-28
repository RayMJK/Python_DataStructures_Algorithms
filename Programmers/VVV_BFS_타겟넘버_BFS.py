def solution(numbers, target):
    result = [0]
    count = 0

    for num in numbers:
        tmp = []
        for i in range(len(result)):
            tmp.append(result[i] + num)
            tmp.append(result[i] - num)
        result = tmp
    for res in result:
        if res == target:
            count += 1

    return count