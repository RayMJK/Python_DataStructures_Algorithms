def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    # print(numbers)
    numbers.sort(key = lambda x:x*3, reverse=True)
    #print(numbers)

    answer = str(int(''.join(numbers)))
    return answer

