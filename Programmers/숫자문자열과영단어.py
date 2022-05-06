def solution(s):
    answer = ''
    hs_map = {
                'zero':0, 'one':1, 'two':2, 'three':3, 'four':4,
                'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9
             }
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    word = ''
    for i in s:
        # print('i = ', i)
        if i in num:
            answer += i
        else:
            word += i
            if word in hs_map:
                # print(word)
                # print(hs_map[word])
                # print(str(hs_map[word]))
                answer += str(hs_map[word])
                word = ''
    answer = int(answer)
    return answer


