import itertools

def solution(numbers):
    answer = ''
    max = 0
    permutation = list(itertools.permutations(numbers))
    print(permutation)
    for i in permutation:
        num = ''
        for j in range(len(i)):
            num += str(i[j])
        print(num)
        if int(num) > max:
            max = int(num)

    answer = str(max)
    print('answer =', answer)
    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))