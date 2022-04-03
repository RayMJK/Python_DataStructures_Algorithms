def solution(tickets):
    answer = []
    tickets.sort()
    print(tickets)
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            print(i)
            answer.append(i)
    print(answer)
    return answer