def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1_b = bin(arr1[i])[2:]
        arr2_b = bin(arr2[i])[2:]
        if len(arr1_b) < n :
            count = n - len(arr1_b)
            a = '0' * count
            arr1_b = a + arr1_b
        if len(arr2_b) < n :
            count = n - len(arr2_b)
            a = '0' * count
            arr2_b = a + arr2_b
        print(arr1_b,arr2_b)
        result = ''
        for j in range(n):
            if arr1_b[j] == '1' or arr2_b[j] == '1':
                result += '#'
            else:
                result += ' '
        answer.append(result)

    return answer


print(solution(5, 	[9, 20, 28, 18, 11], 	[30, 1, 21, 17, 28]))