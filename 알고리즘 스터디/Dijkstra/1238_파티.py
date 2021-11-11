import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra(s, e, dist):
    que = []
    heapq.heappush(que, [0, s])
    dist[s] = 0

    while que:
        d, now = heapq.heappop(que)

        if now == e and e != 999:
            return d

        if dist[now] < d:
            continue

        for v in visited[now]:
            nd = v[1] + d

            if nd < dist[v[0]]:
                dist[v[0]] = nd
                heapq.heappush(que, [nd, v[0]])


N, M, X = map(int, input().split()) # 학생 N명, 단방향 도로 개수 M, 파티 벌이는 마을 X

dist = [float('inf') for _ in range(N + 1)]
visited = [[] for _ in range(N+1)]
for i in range(M):
    s, e, t = map(int, input().split()) # 도로의 시작점 s, 끝점 e, 도로를 지나는 소요시간 t
    visited[s].append([e, t])


'''
time = [0 for _ in range(N+1)]
for i in range(1, N+1):
    dist = [float('inf') for _ in range(N + 1)]
    time[i] += dijkstra(i, X)


    dist = [float('inf') for _ in range(N + 1)]
    time[i] += dijkstra(X, i)

print(max(time))
'''

X_to_i = [float('inf') for _ in range(N + 1)]
dijkstra(X, 999, X_to_i)

answer = 0
for i in range(1, N+1):
    if i == X:
        continue
    dist = [float('inf') for _ in range(N + 1)]
    answer = max(answer, X_to_i[i] + dijkstra(i, X, dist))

print(answer)