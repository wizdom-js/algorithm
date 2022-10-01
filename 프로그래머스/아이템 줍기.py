from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(rectangle, characterX, characterY, itemX, itemY):
    # 최단거리 => bfs
    def bfs(x, y, count):
        queue = deque([[x, y, count]])  # 시작 위치 넣어주기
        while queue:
            x, y, count = queue.popleft()   # 가볼 위치 좌표와 거리 가져오기

            if x == itemX and y == itemY:   # 아이템에 도달한 경우
                return count

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < 102 and 0 <= ny < 102 and board[ny][nx] == 1:  # 테두리를 따라 이동
                    board[ny][nx] = 2   # 갔던 곳 다시 못가게 방문처리
                    queue.append([nx, ny, count + 1])

    # 직사각형 그리기 (간격이 1인 직사각형을 대비하여 두배로 늘려주기)
    board = [[0 for _ in range(102)] for _ in range(102)]
    for rec in rectangle:
        lx, ly, rx, ry = map(lambda x: x * 2, rec)
        for x in range(lx, rx + 1):
            for y in range(ly, ry + 1):
                if lx < x < rx and ly < y < ry: # 직사각형의 내부인 경우
                    board[y][x] = 2
                elif board[y][x] != 2:  # 직사각형의 테두리이고, 다른 직사각형의 내부가 아닌 경우
                    board[y][x] = 1

    itemX, itemY = itemX * 2, itemY * 2
    answer = bfs(characterX * 2, characterY * 2, 0) // 2

    return answer