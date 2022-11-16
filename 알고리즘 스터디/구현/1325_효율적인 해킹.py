import sys
sys.stdin = open('input.txt')


def dfs(com):

    for nxt_com in graph[com]:
        if not visited[nxt_com]:
            visited[nxt_com] = 1
            trust[nxt_com] += trust[com]
            dfs(nxt_com)
            # visited[nxt_com] = 0


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
trust = [0 for _ in range(n+1)]
for _ in range(m):
    com1, com2 = map(int, input().split())
    graph[com1].append(com2)
    trust[com2] += 1

print(trust)

for i in range(1, n+1):
    if trust[i] == 0:
        visited = [0 for _ in range(n + 1)]
        dfs(i)

print(trust)
print(graph)

max_v = max(trust)

for i in range(1, n+1):
    if max_v == trust[i]:
        print(i, end=" ")




