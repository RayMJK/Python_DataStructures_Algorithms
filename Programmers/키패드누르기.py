def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7]
    right = [3, 6, 9]
    l_h = [0, 0]
    r_h = [2, 0]
    for i in numbers:
        if i in left:
            if i == 1:
                l_h[1] = 3
                l_h[0] = 0
            elif i == 4:
                l_h[1] = 2
                l_h[0] = 0
            elif i == 7:
                l_h[1] = 1
                l_h[0] = 0
            answer += 'L'
        elif i in right:
            if i == 3:
                r_h[1] = 3
                r_h[0] = 2
            elif i == 6:
                r_h[1] = 2
                r_h[0] = 2
            elif i == 9:
                r_h[1] = 1
                r_h[0] = 2
            answer += 'R'
        else:  # if i is [2,5,8,0]
            if i == 2:
                if abs(3 - r_h[1]) + abs(1 - r_h[0]) < abs(3 - l_h[1]) + abs(1 - l_h[0]):
                    r_h[0] = 1
                    r_h[1] = 3
                    answer += 'R'
                elif abs(3 - r_h[1]) + abs(1 - r_h[0]) > abs(3 - l_h[1]) + abs(1 - l_h[0]):
                    l_h[0] = 1
                    l_h[1] = 3
                    answer += 'L'
                else:
                    if hand == "right":
                        r_h[0] = 1
                        r_h[1] = 3
                        answer += 'R'
                    else:
                        l_h[0] = 1
                        l_h[1] = 3
                        answer += 'L'
            elif i == 5:
                if abs(2 - r_h[1]) + abs(1 - r_h[0]) < abs(2 - l_h[1]) + abs(1 - l_h[0]):
                    r_h[0] = 1
                    r_h[1] = 2
                    answer += 'R'
                elif abs(2 - r_h[1]) + abs(1 - r_h[0]) > abs(2 - l_h[1]) + abs(1 - l_h[0]):
                    l_h[0] = 1
                    l_h[1] = 2
                    answer += 'L'
                else:
                    if hand == "right":
                        r_h[0] = 1
                        r_h[1] = 2
                        answer += 'R'
                    else:
                        l_h[0] = 1
                        l_h[1] = 2
                        answer += 'L'
            elif i == 8:
                if abs(1 - r_h[1]) + abs(1 - r_h[0]) < abs(1 - l_h[1]) + abs(1 - l_h[0]):
                    r_h[0] = 1
                    r_h[1] = 1
                    answer += 'R'
                elif abs(1 - r_h[1]) + abs(1 - r_h[0]) > abs(1 - l_h[1]) + abs(1 - l_h[0]):
                    l_h[0] = 1
                    l_h[1] = 1
                    answer += 'L'
                else:
                    if hand == "right":
                        r_h[0] = 1
                        r_h[1] = 1
                        answer += 'R'
                    else:
                        l_h[0] = 1
                        l_h[1] = 1
                        answer += 'L'
            else:  # when dial is 0
                if abs(0 - r_h[1]) + abs(1 - r_h[0]) < abs(0 - l_h[1]) + abs(1 - l_h[0]):
                    r_h[0] = 1
                    r_h[1] = 0
                    answer += 'R'
                elif abs(0 - r_h[1]) + abs(1 - r_h[0]) > abs(0 - l_h[1]) + abs(1 - l_h[0]):
                    l_h[0] = 1
                    l_h[1] = 0
                    answer += 'L'
                else:
                    if hand == "right":
                        r_h[0] = 1
                        r_h[1] = 0
                        answer += 'R'
                    else:
                        l_h[0] = 1
                        l_h[1] = 0
                        answer += 'L'

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))