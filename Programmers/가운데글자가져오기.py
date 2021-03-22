def solution(s):
    answer = ''
    length = len(s)
    if length % 2 == 1:
        return s[length//2]
    else:
        return answer+s[:length//2][-1] + s[length//2:][0]
    