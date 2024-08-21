count = 0

def dfs(numbers, target, idx, values):
    global count

    if idx == len(numbers) and values == target:
        count += 1
        return
    elif idx == len(numbers):
        return

    dfs(numbers, target, idx + 1, values + numbers[idx])
    dfs(numbers, target, idx + 1, values - numbers[idx])


def solution(numbers, target):
    global count
    dfs(numbers, target, 0, 0)
    return count
