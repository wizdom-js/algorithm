import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra():
    queue = []
    heapq.heappush(queue, [-999999999999, factory1])
    dist[factory1] = 999999999999

    while queue:
        w, now = heapq.heappop(queue)
        w *= -1

        if now == factory2:
            break

        if dist[now] > w:
            continue

        for nxt, nw in bridge_info[now]:
            nw = min(w, nw)

            if dist[nxt] < nw:
                dist[nxt] = nw
                heapq.heappush(queue, [-nw, nxt])


n, m = map(int, input().split())
bridge_info = [[] for _ in range(n+1)]
for _ in range(m):
    bridge1, bridge2, weight = map(int, input().split())
    bridge_info[bridge1].append([bridge2, weight])
    bridge_info[bridge2].append([bridge1, weight])

factory1, factory2 = map(int, input().split())

for i in range(1, n+1):
    bridge_info[i].sort(key = lambda x: -x[1])

dist = [0 for _ in range(n+1)]
dijkstra()
print(dist[factory2])