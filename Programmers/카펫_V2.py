def solution(brown, yellow):
    answer = []
    #print(brown, yellow)
    
    for i in reversed(range(1, yellow+1)):
        #print(i)
        width = (i+2)
        length = ((yellow/i)+2)
        br = width * length - yellow
        #print(br)
        if br == brown:
            answer.append(width)
            answer.append(length)
            break
    return answer
