def solution(inp_str):
    from string import ascii_lowercase
    from string import ascii_uppercase

    lower_alpha = list(ascii_lowercase)
    upper_alpha = list(ascii_uppercase)
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    char = '~!@#$%^&*'
    answer = []
    kind = []
    count = 0
    pw = list(set(inp_str))
    pw.sort()
    count_dict = dict()
    stack = []
    stack.append(inp_str[0])
    print(inp_str)
    for i in range(1,len(inp_str)):
        if inp_str[i] == stack[-1]:
            count += 1
            stack.append(inp_str[i])
            if count == 4:
                answer.append(4)
        else:
            count = 1
            stack.append(inp_str[i])
    print(stack)
    for i in inp_str:
        if count_dict.get(i) == None:
            count_dict[i] = 1
        else:
            count_dict[i] += 1
    max = -1
    for key in count_dict:
        if count_dict[key] > max:
            max = count_dict[key]

    if max >= 5:
        answer.append(5)

    if len(inp_str) < 8 or len(inp_str) > 15:
        answer.append(1)
    for i in pw:
        if i in lower_alpha:
            kind.append(2)
        elif i in upper_alpha:
            kind.append(1)
        elif i in num:
            kind.append(3)
        elif i in char:
            kind.append(4)
        else:
            kind.append(5)

    if 5 in kind:
        answer.append(2)
        kind.remove(5)
        if len(kind) < 3:
            answer.append(3)

    return sorted(answer)


inp_str = "aaaaZZZZ)"
print(solution(inp_str))
