def solution(a, edges):
    def dfs(x, a):
        nonlocal answer

        now = a[x]
        visited[x] = 1

        for i in graph[x]:
            if visited[i] == 0:
                now += dfs(i, a)

        answer += abs(now)

        return now

    if sum(a) != 0:
        return -1

    n = len(a)
    graph = [[] for _ in range(n)]

    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    answer = 0
    visited = [0 for _ in range(n)]
    dfs(0, a, graph)

    return answer