def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left = 1
    right = distance

    while left <= right:
        mid = (left + right) // 2
        remove_cnt = 0
        standard = 0
        for rock in rocks:
            if rock - standard < mid:
                remove_cnt += 1
            else:
                standard = rock

            if remove_cnt > n:
                break

        if remove_cnt > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer