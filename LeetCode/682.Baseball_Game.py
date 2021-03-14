def calPoints(ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    result = []
    for i in range(len(ops)):
        if ops[i] == "+":
            result.append(int(result[-2]) + int(result[-1]))

        elif ops[i] == "D":
            result.append(int(result[-1]) * 2)


        elif ops[i] == "C":
            result.remove(result[-1])

        else:
            result.append(int(ops[i]))


    return sum(result)

print(calPoints(["5","2","C","D","+"]))