import sys
sys.stdin = open('sample_input.txt')


dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

import heapq
from collections import deque

def dijkstra(y, x):
    heap = []
    heapq.heappush(heap, [y, x])
    visited[y][x] = 0
    while heap:
        y, x = heapq.heappop(heap)

        if y == n-1 and x == n-1:
            return

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                h = 0
                if heights[y][x] < heights[ny][nx]:
                    h = heights[ny][nx] - heights[y][x]
                if visited[ny][nx] > visited[y][x] + 1 + h:
                    visited[ny][nx] = visited[y][x] + 1 + h
                    heapq.heappush(heap, [ny, nx])


def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = 0
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                h = 0
                if heights[y][x] < heights[ny][nx]:
                    h = heights[ny][nx] - heights[y][x]
                if visited[ny][nx] > visited[y][x] + 1 + h:
                    visited[ny][nx] = visited[y][x] + 1 + h
                    queue.append((ny, nx))


tc = int(input())
for idx in range(1, tc+1):
    n = int(input())
    heights = [list(map(int, input().split())) for _ in range(n)]
    visited = [[float('inf') for _ in range(n)] for _ in range(n)]
    ######## bfs ############
    # bfs(0, 0)

    ######## dijkstra ############
    dijkstra(0, 0)

    print('#{} {}'.format(idx, visited[-1][-1]))