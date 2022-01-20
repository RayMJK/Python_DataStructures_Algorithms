def solution(prices):
    answer = []
    stack = []
    for i in range(len(prices)-1):
        if len(stack) != 0 :
            stack.pop()
        stack.append(prices[i])
        a = 0
        flag = -1
        for j in range(i+1, len(prices)):
            #print(stack)
            if stack[0] > prices[j]:
                flag = 0
                #print(i, j-i)
                answer.append(j-i)
                stack.pop()
                break
            else:
                a+=1
        if flag == -1:
            answer.append(a)
        #print(answer)
    answer.append(0)            
    return answer
