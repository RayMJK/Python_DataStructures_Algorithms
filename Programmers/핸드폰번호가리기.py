def solution(phone_number):
    answer = ''
    for i in phone_number[:-4]:
        answer+='*'
    for i in phone_number[-4:]:
        answer+=i
    return answer