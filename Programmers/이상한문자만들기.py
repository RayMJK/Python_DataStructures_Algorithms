def solution(s):
    answer = ''
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == ' ':
                answer += s[i]
            else:
                answer += s[i].upper()
        else:
            if s[i] == ' ':
                answer += s[i]
            else:
                answer += s[i].lower()

    return answer

print(solution("try hello world"))