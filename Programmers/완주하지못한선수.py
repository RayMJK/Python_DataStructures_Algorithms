def solution(participant, completion):
    answer = ''
    i = 0
    while len(participant) > 1:
        if participant[0] not in completion:
            return answer + participant[0]
        else:
            completion.remove(participant[0])
            del participant[0]
    return participant[0]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))