from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, place):
    queue = deque([[x, y]])
    visited = [[False for _ in range(5)] for _ in range(5)]
    depth = 0
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = True
                if place[nx][ny] == 'P':
                    return 0
                elif place[nx][ny] == 'O':
                    if depth < 1:
                        queue.append([nx, ny])

        depth += 1
    return 1


def solution(places):
    answer = []

    for place in places:
        tmp = 1
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    tmp = bfs(x, y, place)
                if tmp == 0:
                    break
            if tmp == 0:
                break
        answer.append(tmp)
    return answer

