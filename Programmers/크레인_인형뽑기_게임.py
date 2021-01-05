board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]
#result = [4, 3, 1, 1, 3, 2, 4]
# re result = [4, 2, 4]

result=[]
answer = 0

for i in moves:
    j = 0
    while board[j][i - 1] == 0 and j < len(board)-1:
        j += 1
    if board[j][i - 1] != 0:
        add_val = board[j][i - 1]
        board[j][i - 1] = 0
        if len(result)!=0 :  # result에 요소가 최소 한개이상 있을때
            result_top = result.pop()  # 맨 위 요소 확인
            if result_top != add_val:  # 맨 위 요소가 추가 요소와 다를때
                result.append(result_top)
                result.append(add_val)

            else:   # 맨 위 요소가 추가 요소와 같을때
                answer += 2
        else:
            result.append(add_val)
print(result)
        #result.append(board[j][i - 1])
'''
        if result:
            result_top = result.pop()
            if result_top == board[j][i-1]:
                answer += 2
            else :
                result.append(board[j][i-1])
        else:
            result.append(board[j][i - 1])

    board[j][i - 1] = 0

print(result)
'''