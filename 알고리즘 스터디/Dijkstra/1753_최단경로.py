import sys
sys.stdin = open('input.txt')

import heapq


def dijkstra():
    que = []
    heapq.heappush(que, [0, k])
    dist[k] = 0

    while que:
        d, now = heapq.heappop(que)

        if dist[now] < d:
            continue

        for v in visited[now]:
            nd = v[1] + d

            if nd < dist[v[0]]:
                dist[v[0]] = nd
                heapq.heappush(que, [nd, v[0]])


v, e = map(int, input().split())    # 정점 개수 v, 간선의 개수 e
k = int(input())    # 시작 정점의 번호 k
dist = [float('INF') for _ in range(v+1)]

visited = [[] for _ in range(v+1)]
for i in range(e):
    u, v, w = map(int, input().split()) # u에서 v로 가는 가중치 w
    visited[u].append([v, w])

dijkstra()

for i in dist[1:]:
    if i == float('INF'):
        print('INF')
    else:
        print(i)
