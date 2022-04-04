def solution(tickets):
    answer = []
    tickets.sort()
    # print(tickets)
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            #print(i)
            answer.append(tickets[i][0])
            answer.append(tickets[i][1])
            tickets.pop(i)
            break
    # tickets.remove(tickets[i])
    # print(answer)
    # print(tickets)
    while tickets:
        for i in tickets:
            # print(i)
            if i[0] == answer[-1]:
                answer.append(i[1])
                tickets.remove(i)
                break
    
    return answer
