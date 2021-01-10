def solution(skill, skill_trees):
    answer = 0

    skill_list = list(skill)

    for a_skill in skill_trees:
        print(a_skill)
        index = -1
        succeed = 0
        exist = -1
        for s in skill_list:
            if s in a_skill:
                exist = 1
        if exist == -1:
            answer += 1

        for j in range(len(a_skill)):
            if skill_list[0] not in a_skill:
                break
            if a_skill[j] in skill_list:
                if skill_list.index(a_skill[j]) == index+1 :
                    index = skill_list.index(a_skill[j])
                    succeed = 1
                else:
                    succeed = 0
                    break
        if succeed == 1:
            answer += 1

    return answer


skill = 'CBD'
skill_trees =["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))