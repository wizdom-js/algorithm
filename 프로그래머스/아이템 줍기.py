from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(rectangle, characterX, characterY, itemX, itemY):
    def bfs(x, y, count):
        queue = deque([[x, y, count]])
        while queue:
            x, y, count = queue.popleft()

            if x == itemX and y == itemY:
                return count

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < 102 and 0 <= ny < 102:
                    if board[ny][nx] == 1:
                        board[ny][nx] = 2
                        queue.append([nx, ny, count + 1])
        return 0

    board = [[0 for _ in range(102)] for _ in range(102)]
    for rec in rectangle:
        lx, ly, rx, ry = map(lambda x: x * 2, rec)
        for x in range(lx, rx + 1):
            for y in range(ly, ry + 1):
                if lx < x < rx and ly < y < ry:
                    board[y][x] = 2
                elif board[y][x] != 2:
                    board[y][x] = 1

    itemX, itemY = itemX * 2, itemY * 2
    answer = bfs(characterX * 2, characterY * 2, 0) // 2

    return answer