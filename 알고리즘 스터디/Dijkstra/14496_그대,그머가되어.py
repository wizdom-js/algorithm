import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra():
    dist = [float('inf') for _ in range(n+1)]
    queue = []
    heapq.heappush(queue, [0, a])
    dist[a] = 0
    while queue:
        d, now = heapq.heappop(queue)

        if now == b:
            print(d)
            return

        if d < dist[now]:
            continue

        for next in visited[now]:
            nd = d + 1
            if nd < dist[next]:
                dist[next] = nd
                heapq.heappush(queue, [nd, next])
    print(-1)
    return


a, b = map(int, input().split())
n, m = map(int, input().split())

visited = [[] for _ in range(n+1)]
for _ in range(m):
    t1, t2 = map(int, input().split())
    visited[t1].append(t2)
    visited[t2].append(t1)

dijkstra()