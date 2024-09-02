
# https://cocook.tistory.com/84
'''
기준은 n개의 돌을 징검다리에서 제거했을 때 최소 거리이다. 먼저 범위를 생각해보면 최소값은 징검다리에 돌이 겹쳐있는 경우는 없기 때문에 1이다.
최대 값은 시작지점과 도착지점사이의 거리인 distance이다.
이 값을 기준으로 중간값(mid)가 n개의 돌을 제거했을 때 돌 사이의 거리중 최소값이라고 가정해보자.

이 가정하에 돌을 제거했을 때 이 값(mid)보다 작은 거리는 없어야 한다.

즉 돌 사이의 거리를 구했을 때 이 mid 값보다 작으면 제거하고 크면 두는 방식의 전략을 사용해야한다.

돌 사이의 거리를 모두 재는 것은 무의미하므로 시작지점(0)으로부터 mid값 보다 먼 거리에 있는 돌을 찾기 전까지 돌을 제거하고 찾으면 그 돌을 새로운 기준으로 삼아 다시 돌 사이의 거리를 측정하면 된다.
'''

def solution(distance, rocks, n):
    # 커트라인 최솟값 = 1
    left = 1
    # 커트라인 최댓값 = distance
    right = distance

    # 바위 위치를 정렬하고, 도착지점 append
    rocks.sort()
    rocks.append(distance)

    while left <= right:
        mid = (left+right)//2
        # 제거한 바위 개수
        delete = 0
        # 이전 바위의 위치
        prev_rock = 0 #기준이되는 돌(시작지점)
        for rock in rocks:
            dist = rock - prev_rock
            #돌사이의 거리가 가정한 값보다 작으면 제거한다.
            if dist < mid:
                delete += 1
                # 제거한 바위가 너무 많다면 break
                if delete > n:
                    break
            #아니라면 그 돌을 새로운 기준으로 세운다.
            else:
                prev_rock = rock

        # 초과 제거한 경우 : 커트라인이 너무 높음
        #제거된 돌이 너무 많으면 가정한 값이 큰 것이므로 범위를 작은 쪽으로 줄인다.
        if delete > n:
            right = mid -1
        #반대라면 큰 쪽으로 줄인다.
        else:
            answer = mid
            left = mid + 1
    return answer