def solution(skill, skill_trees):
    answer = 0

    skill_list = list(skill)

    for a_skill in skill_trees:
        print(a_skill)
        index = 0
        for j in range(len(a_skill)):
            if a_skill[j] in skill_list:
                if skill_list.index(a_skill[j]) > index:
                    index = skill_list.index(a_skill[j])
                else:
                    break

        answer += 1

    return skill_list


skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print('skill_list = ', solution(skill, skill_trees))