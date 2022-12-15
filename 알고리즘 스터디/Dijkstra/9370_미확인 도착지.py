import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra(s):
    queue = []
    dist = [float('inf') for _ in range(n + 1)]

    heapq.heappush(queue, (0, s))
    dist[s] = 0

    while queue:
        d, now = heapq.heappop(queue)

        if dist[now] < d:
            continue

        for nxt, nd in graph[now]:
            nd += d

            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(queue, (nd, nxt))

    return dist


tc = int(input())
for _ in range(tc):
    # 정점의 개수 n, 간선의 개수 m, 목적지 후보 개수 t
    n, m, t = map(int, input().split())
    # 출발지 s, 지나간 도로 g, h
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    # 목적지 후보
    destinations = []
    for _ in range(t):
        destinations.append(int(input()))

    start = dijkstra(s)
    start_g = dijkstra(g)
    start_h = dijkstra(h)

    answer = []
    for d in destinations:
        if start[g] + start_g[h] + start_h[d] == start[d] or start[h] + start_g[d] + start_h[g] == start[d]:
            if start[d] != float('inf'):
                answer.append(d)

    answer.sort()
    print(*answer)