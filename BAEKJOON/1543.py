document = input()
word = input()

answer = 0
length = len(word)

while len(document) >= length:
    if document[:length] == word:
        answer += 1
        document = document[length:]
    else:
        document = document[1:]

print(answer)