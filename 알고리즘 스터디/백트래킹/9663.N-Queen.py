import sys
sys.stdin = open('input.txt')

from collections import deque
import copy
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

def dfs(cnt):
    global answer
    if cnt == n:
        answer += 1
        return

    for i in range(n):
        if visited[i]:
            continue
        idx[cnt] = i
        for j in range(n):
            if abs(idx[cnt] - idx[j]) == cnt - j:
                break
        else:
            visited[j] = True
            dfs(cnt + 1)
            visited[j] = False


n = int(input())
visited = [False for _ in range(n)]
idx = [0 for _ in range(n)]
answer = 0
dfs(0)
print(answer)