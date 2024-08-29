def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        a = commands[i][0]-1
        b = commands[i][1]-1
        c = commands[i][2]-1
        tmp = array[a:b+1]
        tmp.sort()
        answer.append(tmp[c])

    return answer

