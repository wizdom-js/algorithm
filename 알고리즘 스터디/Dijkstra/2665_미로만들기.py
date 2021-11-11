import sys
sys.stdin = open('input.txt')

import heapq

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dijkstra():
    que = []
    heapq.heappush(que, [0, 0, 0])
    dist[0][0] = 0

    while que:
        d, y, x = heapq.heappop(que)

        if dist[y][x] < d:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                room = 0 if rooms[ny][nx] else 1
                # room = 1 ^ rooms[ny][nx]  # 같으면 0 다르면 1
                nd = d + room

                if nd < dist[ny][nx]:
                    dist[ny][nx] = nd
                    heapq.heappush(que, [nd, ny, nx])


n = int(input())    # 검은 방의 수
rooms = [list(map(int, input())) for _ in range(n)]

dist = [[float('inf') for _ in range(n)] for _ in range(n)]

dijkstra()
print(dist[n-1][n-1])


