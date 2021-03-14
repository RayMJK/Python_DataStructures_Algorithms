import operator
def slowestKey(releaseTimes, keysPressed):
    """
    :type releaseTimes: List[int]
    :type keysPressed: str
    :rtype: str
    """
    answer_dict = dict()
    for i in range(len(releaseTimes)):
        if i == 0:
            answer_dict[keysPressed[i]] = releaseTimes[i]
            print(answer_dict)
        else:
            if keysPressed[i] not in answer_dict:
                answer_dict[keysPressed[i]]=releaseTimes[i]-releaseTimes[i-1]
            else:
                if answer_dict[keysPressed[i]] > releaseTimes[i]-releaseTimes[i-1]:
                    pass
                else:
                    answer_dict[keysPressed[i]] = releaseTimes[i] - releaseTimes[i - 1]
                print(answer_dict)
    print(answer_dict)
    result = [k for k, v in answer_dict.items() if max(answer_dict.values()) == v]
    answer = sorted(result)[-1]
    return answer


print(slowestKey([19,22,28,29,66,81,93,97],"fnfaaxha"))