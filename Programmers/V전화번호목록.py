def solution(phone_book):
    answer = True
    phone_book.sort()
    #print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1][:len(phone_book)]:
            return False
    return answer
