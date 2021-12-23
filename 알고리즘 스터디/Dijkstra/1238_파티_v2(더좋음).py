import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra(s, e):
    dist = [float('inf') for _ in range(n+1)]
    queue = []
    heapq.heappush(queue, [0, s])
    dist[s] = 0
    while queue:
        d, now = heapq.heappop(queue)

        if now == e:
            return d

        if dist[now] < d:
            continue

        for next in visited[now]:
            nd = next[1] + d

            if nd < dist[next[0]]:
                dist[next[0]] = nd
                heapq.heappush(queue, [nd, next[0]])
    return dist

n, m, x = map(int, input().split())

visited = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    visited[s].append([e, t])

x_to_s = dijkstra(x, 0)

answer = 0
for i in range(1, n+1):
    distance = dijkstra(i, x) + x_to_s[i]
    answer = max(answer, distance)

print(answer)
