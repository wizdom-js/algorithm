import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra(s, e):
    que = []
    heapq.heappush(que, [0, s])
    dist[s] = 0

    while que:
        d, now = heapq.heappop(que)

        if now == e:
            return d

        if d > dist[now]:
            continue

        for i in visited[now]:
            nd = dist[now] + i[1]

            if dist[i[0]] > nd:
                dist[i[0]] = nd
                heapq.heappush(que, [nd, i[0]])

N, M, X = map(int, input().split()) # 학생 N명, 단방향 도로 개수 M, 파티 벌이는 마을 X


dist = [float('inf') for i in range(N + 1)]
visited = [[] for i in range(N+1)]
for i in range(N):
    s, e, t = map(int, input().split()) # 도로의 시작점 s, 끝점 e, 도로를 지나는 소요시간 t
    visited[s].append([e, t])

print(visited)

for i in range(1, N+1):
    answer = dijkstra(i, e) + dijkstra(e, i)
    print(answer)


print(dist)