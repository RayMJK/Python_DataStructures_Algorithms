from string import ascii_lowercase


def solution(new_id):
    answer = ''
    new_id.lower()  # step 1
    id_list = list(ascii_lowercase)
    id_list.append('-')
    id_list.append('_')
    id_list.append('.')
    new_id.replace('.', ' ')  # step 3
    for i in range(len(new_id)):
        if new_id[i] not in id_list:  # step 2
            new_id = new_id.replace(new_id[i], ' ')
    if len(new_id) == 0:  # step 5
        new_id = 'a'

    return answer