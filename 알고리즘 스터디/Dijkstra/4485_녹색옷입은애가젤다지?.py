import sys
sys.stdin = open('input.txt')


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

import heapq

def dijkstra():
    queue = []
    heapq.heappush(queue, [rupee[0][0], 0, 0])
    visited[0][0] = 0

    while queue:
        d, y, x = heapq.heappop(queue)

        if y == n-1 and x == n-1:
            print(f'Problem {tc}: {d}')
            return

        if d < visited[y][x]:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                nd = d + rupee[ny][nx]
                if nd < visited[ny][nx]:
                    visited[ny][nx] = nd
                    heapq.heappush(queue, [nd, ny, nx])

tc = 1
while True:
    n = int(input())
    if n == 0:
        break
    rupee = [list(map(int, input().split())) for _ in range(n)]

    visited = [[float('inf') for _ in range(n)] for _ in range(n)]
    dijkstra()

    tc += 1


def dfs(y, x, k):
    global answer
    global end

    if end and answer < k:
        return

    if y == n-1 and x == n-1:
        end = True
        if k < answer:
            answer = k
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, k + rupee[ny][nx])
            visited[ny][nx] = False

# tc = 1
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     rupee = [list(map(int, input().split())) for _ in range(n)]
#
#     visited = [[False for _ in range(n)] for _ in range(n)]
#     answer = 99999999999
#     end = False
#     dfs(0, 0, rupee[0][0])
#     print(f'Problem {tc}: {answer}')
#
#     tc += 1



