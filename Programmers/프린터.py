def solution(priorities, location):
    answer = 0
    zipfile = []
    for pr, i in zip(priorities, range(len(priorities))):
        zipfile.append((pr, i))
    print(zipfile)

    while True:
        maximum = max(zipfile, key=lambda x: x[0])
        if zipfile[0][0] < maximum[0]:
            b = zipfile.pop(0)
            zipfile.append(b)
        else:
            answer += 1
            if zipfile[0][1] != location:
                zipfile.pop(0)
            else:
                a = zipfile[0][1]
                break
        # print(zipfile)
    return answer