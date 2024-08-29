def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i, citation in enumerate(citations):
        if citation >= i+1:
            h_index = i+1
            answer = h_index
    return answer