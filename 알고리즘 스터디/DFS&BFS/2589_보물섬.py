import sys
sys.stdin = open('input.txt')

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(sy, sx, hour):
    queue = deque([(sy, sx, hour)])
    visited = [[0 for _ in range(garo)] for _ in range(sero)]
    visited[sy][sx] = 1
    while queue:
        y, x, hour = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < sero and 0 <= nx < garo:
                if treasure_map[ny][nx] == 'W' or visited[ny][nx]:
                    continue
                visited[ny][nx] = 1
                queue.append((ny, nx, hour+1))
    return hour


sero, garo = map(int, input().split())
treasure_map = [input() for _ in range(sero)]

answer = 0
for h in range(sero):
    for w in range(garo):
        if treasure_map[h][w] == 'L':
            answer = max(answer, bfs(h, w, 0))

print(answer)