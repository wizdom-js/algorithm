import sys
sys.stdin = open('input.txt')

import heapq

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

m, n = map(int, input().split())    # 가로 m, 세로 n
maze = [list(map(int, input())) for _ in range(n)]  # 미로
dist = [[999999999999 for _ in range(m)] for _ in range(n)]

que = []
heapq.heappush(que, [0, 0, 0])  # 벽인지 아닌지(가중치), y, x
dist[0][0] = 0

while que:
    d, y, x = heapq.heappop(que)

    if y == n-1 and x == m-1:
        print(d)
        break

    if dist[y][x] < d:
        continue

    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 <= ny < n and 0 <= nx < m:
            nd = maze[ny][nx] + d

            if nd < dist[ny][nx]:
                dist[ny][nx] = nd
                heapq.heappush(que, [nd, ny, nx])
