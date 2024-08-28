from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 제한사항에서 모든 좌표값은 1 이상 50 이하라고 했고 2배의 좌표를 그려야 하므로 102*102 크기의 2차원 배열 선언

    graph = [[-1]*102 for _ in range(102)]
    visited =[[1]*102 for _ in range(102)] # 아직 방문하지 않은 곳은 1로 표시
    directions = [(0,-1), (0,1), (1,0), (-1,0)]

    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, r)
        for i in range(x1, x2+1) :
            for j in range(y1, y2+1):
                # x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 현재 직사각형의 테두리일 때 1로 채움
                elif graph[i][j] != 0 :
                    graph[i][j] = 1

    # 반복문을 마치면 테두리는 1, 내부는 0, 외부는 -1이 될 것이다

    # 캐릭터와 아이템의 좌표도 2배씩 늘린다
    cx, cy = 2*characterX, 2*characterY
    ix, iy = 2 * itemX, 2*itemY

    q = deque()
    q.append((cx, cy))

    while q:
        x, y = q.popleft()
        # 도착한 곳이 아이템이 있는 장소라면 현재의 최단거리(나누기 2)를 answer로 하고 while문을 빠져나옴
        if x == ix and y == iy:
            answer = visited[x][y] // 2
            break
        for dx, dy in directions:
            nx, ny = x+dx, y+dy

            # 현재 좌표가 테두리이고 아직 방문하지 않은 곳이라면 q에 추가 후 visited를 최단거리로 갱신
            if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] += visited[x][y]
                q.append((nx,ny))

    return answer

