def solution(s):
    answer = ''
    result = s.split(' ')
    for word in result:
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()

        answer += ' '
    answer = answer[:-1]
    return answer