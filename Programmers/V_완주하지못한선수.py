def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if completion[i] != participant[i]:
            answer = participant[i]
            return answer

    answer = participant[-1]
    return answer