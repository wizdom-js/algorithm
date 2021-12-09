import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    visited = [[False for _ in range(w)] for _ in range(h)]
    queue = deque([(0, 0)])
    melted = 0
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if cheese[ny][nx] == 0 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                elif cheese[ny][nx] == 1:
                    cheese[ny][nx] = 0
                    melted += 1
                    visited[ny][nx] = True
    return melted


h, w = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(h)]

time = 0
mc = 0
while True:
    tmp = bfs()
    if tmp == 0:
        break
    mc = tmp
    time += 1

print(time)
print(mc)