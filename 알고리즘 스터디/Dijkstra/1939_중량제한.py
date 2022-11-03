import sys
sys.stdin = open('input.txt')

import heapq
from collections import deque


def dijkstra():
    dist = [0 for _ in range(n + 1)]
    dist[factory1] = 999999999999

    queue = []
    heapq.heappush(queue, [-999999999999, factory1])

    while queue:
        w, now = heapq.heappop(queue)
        w *= -1

        if now == factory2:
            return now

        if dist[now] > w:
            continue

        for nxt, nw in bridge_info[now]:
            nw = min(w, nw)

            if dist[nxt] < nw:
                dist[nxt] = nw
                heapq.heappush(queue, [-nw, nxt])


def bfs(weight):
    visited = [0 for _ in range(n + 1)]
    visited[factory1] = True

    queue = deque([factory1])
    while queue:
        now = queue.popleft()

        if now == factory2:
            return True

        for nxt, nxt_w in bridge_info[now]:
            if not visited[nxt] and weight <= nxt_w:
                visited[nxt] = True
                queue.append(nxt)

    return False


n, m = map(int, input().split())
bridge_info = [[] for _ in range(n+1)]
for _ in range(m):
    bridge1, bridge2, weight = map(int, input().split())
    bridge_info[bridge1].append([bridge2, weight])
    bridge_info[bridge2].append([bridge1, weight])

factory1, factory2 = map(int, input().split())


for i in range(1, n+1):
    bridge_info[i].sort(key = lambda x: -x[1])

# 풀이 1 => 다익스트라
# print(dijkstra())

# 풀이 2 => BFS + 이분탐색
low, high = 1, 1000000000
while low <= high:
    mid = (low + high) // 2
    if bfs(mid):
        low = mid + 1
    else:
        high = mid - 1

print(low, high)
