import sys
sys.stdin = open('input.txt')

from collections import deque


def dfs(com):
    for nxt_com in graph[com]:
        if not visited[nxt_com]:
            visited[nxt_com] = 1
            trust[nxt_com] += trust[com]
            dfs(nxt_com)
            # visited[nxt_com] = 0


def bfs(s):
    visited = [0 for _ in range(n+1)]
    visited[s] = True

    queue = deque([s])
    while queue:
        now = queue.popleft()

        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

    return sum(visited)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
# trust = [0 for _ in range(n+1)]
for _ in range(m):
    com1, com2 = map(int, input().split())
    graph[com2].append(com1)
    # trust[com2] += 1

# print(trust)

answer = []
max_v = 0
for i in range(1, n+1):
    tmp_v = bfs(i)
    if max_v < tmp_v:
        answer = [i]
        max_v = tmp_v
    elif max_v == tmp_v:
        answer.append(i)
#
# print(trust)
# print(graph)

# max_v = max(trust)

# for i in range(1, n+1):
#     if max_v == trust[i]:
#         print(i, end=" ")


print(*answer)


