def solution(nums):
    nums.sort()
    last = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j+1, len(nums)):
                result = nums[i] + nums[j] + nums[k]
                answer = -1
                print('i,j,k', nums[i], nums[j], nums[k], result)
                for m in range(2, result):
                    if result % m == 0:
                        answer = 1
                        break
                if answer == -1:
                    last += 1
    return last

print(solution([1,2,7,6,4]))