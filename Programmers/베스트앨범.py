def solution(genres, plays):
    answer = []
    a = dict()
    hm = dict()
    hm_g = dict()
    hm_p = dict()
    for i in range(len(genres)):

        hm_g[i] = genres[i]
        hm_p[i] = plays[i]
        if genres[i] not in hm:
            a[genres[i]] = []
            hm[genres[i]] = plays[i]
        else:
            hm[genres[i]] += plays[i]

    # print(hm)
    hm = sorted(hm.items(), key=lambda x: x[1], reverse=True)
    '''
    print(hm)
    print(hm_g)
    print(hm_p)
    '''
    # print(a)
    # for i in hm:
    # print(i[0])

    for i in a:
        for j in range(len(genres)):
            if genres[j] == i:
                a[i].append(j)
    # print(a)

    for i in hm:
        b = []
        for j in a[i[0]]:
            # print(j)
            b.append((j, hm_p[j]))
        # print(b)
        b = sorted(b, key=lambda x: x[1], reverse=True)
        # print(b)
        if len(b) > 1:
            c = b.pop(0)[0]
            d = b.pop(0)[0]
            answer.append(c)
            answer.append(d)
        else:
            e = b.pop()[0]
            answer.append(e)
    return answer