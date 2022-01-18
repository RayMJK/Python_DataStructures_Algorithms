def solution(genres, plays):
    answer = []
    hm = dict()
    hm_g = dict()
    hm_p = dict()
    for i in range(len(genres)):
        hm_g[i] = genres[i]
        hm_p[i] = plays[i]
        if genres[i] not in hm:
            hm[genres[i]] = plays[i]
        else:
            hm[genres[i]] += plays[i]

    # print(hm)
    hm = sorted(hm.items(), key=lambda x: x[1], reverse=True)
    print(hm)
    print(hm_g)
    print(hm_p)

    # for i in hm:
    # print(i[0])

    return answer