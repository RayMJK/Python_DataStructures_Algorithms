from string import ascii_lowercase


def solution(new_id):
    answer = ''
    new_id = new_id.lower()  # step 1
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]

    id_list = list(ascii_lowercase)
    id_list = id_list + num
    id_list.append('-')
    id_list.append('_')
    id_list.append('.')
    if len(new_id) == 0:  # step 5
        new_id = 'a'
    for i in range(len(new_id)):
        if new_id[i] not in id_list:  # step 2
            new_id = new_id.replace(new_id[i], ' ')
    a = new_id.split()
    new_id = ''.join(a)
    new_id = new_id.replace('.', ' ')  # step 3

    b = new_id.split()

    for i in range(len(b)):  # step 4
        answer += b[i]
        if i != len(b) - 1:
            answer += '.'
    if len(answer) >= 16: # step 6
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    if len(answer) == 0:
        return 'aaa'
    elif len(answer) <= 2: # step 7
        answer += answer[-1] * (3 - len(answer))

    return answer