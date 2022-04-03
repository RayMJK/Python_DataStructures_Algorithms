def solution(tickets):
    answer = []
    a = []
    tickets.sort()
    print(tickets)
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            print(i)
            a.append(tickets[i][0])
            a.append(tickets[i][1])
            break
    print(a)

    return answer