import sys
sys.stdin = open('input.txt')

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
answer = 1e9

def dfs(s, now, total):
    global answer

    if answer < total:
        return

    if s == now and False not in visited:
        if total < answer:
            answer = total
        return

    for i in range(n):
        if not cost[now][i]:
            continue

        if visited[i]:
            continue

        visited[i] = True
        dfs(s, i, total + cost[now][i])
        visited[i] = False

dfs(0, 0, 0)
print(answer)