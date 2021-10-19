import sys
sys.stdin = open('input.txt')

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(sy, sx):
    queue = deque([sy, sx, 19])
    while queue:
        y, x, beer = deque.popleft()
        if beer == 0:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 32767 and 0 <= nx < 32767 and not visited[ny][nx]:
                if point[ny][nx] == 'p':
                    visited[ny][nx] = 1
                    queue.append([ny, nx, 19])
                elif point[ny][nx] == 'e':
                    return 'happy'
                else:
                    visited[ny][nx] = 1
                    queue.append([ny, nx, beer-1])
    return 'sad'



tc = int(input())
for tc_n in range(1, tc+1):
    n = int(input())
    point = [[0 for _ in range(32767)] for _ in range(32767)]
    for i in range(n+2):
        if i == 0:
            sx, sy = map(int, input().split())
            point[sy//50][sx//50] = 's'
        elif i == n+1:
            x, y = map(int, input().split())
            point[y//50][x//50] = 'e'
        else:
            x, y = map(int, input().split())
            point[y//50][x//50] = 'p'

    visited = [[0 for _ in range(32767)] for _ in range(32767)]

    print(bfs(sy, sx))