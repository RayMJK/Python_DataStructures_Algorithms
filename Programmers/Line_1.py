def solution(table, languages, preference):
    answer = ''
    tb = []
    job_dict = dict()

    for i in range(len(table)):
        tb.append(table[i].split(' '))
    for j in tb:
        grade_sum = 0
        for i in range(len(languages)):
            if languages[i] in j:
                score = 6 - j.index(languages[i])
                # print('preference=', preference[i])
                grade_sum += score * preference[i]
                # print(score)
            else:
                score = 0
                # print('preference=', preference[i])
                grade_sum += score * preference[i]
                # print(score)
        job_dict[j[0]] = grade_sum
        # print(job_dict)
    result = [k for k, v in job_dict.items() if max(job_dict.values()) == v]
    result.sort()
    result = result[0]
    # print(result)
    answer += result

    return answer

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]

print(solution(table, languages, preference))

# tb =
# [['SI', 'JAVA', 'JAVASCRIPT', 'SQL', 'PYTHON', 'C#'],
# ['CONTENTS', 'JAVASCRIPT', 'JAVA', 'PYTHON', 'SQL', 'C++'],
# ['HARDWARE', 'C', 'C++', 'PYTHON', 'JAVA', 'JAVASCRIPT'],
# ['PORTAL', 'JAVA', 'JAVASCRIPT', 'PYTHON', 'KOTLIN', 'PHP'],
# ['GAME', 'C++', 'C#', 'JAVASCRIPT', 'C', 'JAVA']]