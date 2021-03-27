def solution(s, n):
    answer = ''
    for i in s :
        if i != ' ' :
            state = ord(i)
            if state <= 90:
                if state+n <= 90:
                    answer += chr(state+n)
                else:
                    answer += chr(state+n-26)
            elif 97<= state <= 122:
                if state+n <= 122:
                    answer += chr(state+n)
                else:
                    answer += chr(state+n-26)
        else:
            answer += ' '
    return answer