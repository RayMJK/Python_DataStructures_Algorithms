def solution(numbers):
    answer = []
    numbers.sort()
    #[1,1,2,3,4]

    #[1, 2, 3, 4]
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            new_sum = numbers[i]+numbers[j]
            #print(new_sum)
            answer.append(new_sum)
    #print(answer)
    answer = sorted(list(set(answer)))
    return answer

print(solution([2,1,3,4,1]))