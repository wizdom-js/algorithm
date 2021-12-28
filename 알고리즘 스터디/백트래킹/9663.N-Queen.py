import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [1, 0]
dy = [0, 1]


#
# def bfs():
#     queue = deque([(0, 0)])
#     while queue:
#         y, x = queue.popleft()
#         for i in range(4):
#             ny = dy[i] + y
#             nx = dx[i] + x
#             if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
#                 visited[ny][nx] = True
#                 queue.append((y, x))
#

def dfs(y):
    global answer
    if y == n:
        answer += 1
        return

    # for i in range(4):
    #         ny = dy[i] + y
    #         nx = dx[i] + x
    #         if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
    #             visited[ny][nx] = True
    #             dfs(ny, nx, )
    for i in range(n):
        if not visited[y][i]:
            visit(y)
            dfs(y+1)

def visit(x):
    for i in range(n):
        visited[i][x] = True
        if i == x:
            x += 1
            visited[i][x] = True


n = int(input())
visited = [[False for _ in range(n)] for _ in range(n)]
answer = 0

print(answer)