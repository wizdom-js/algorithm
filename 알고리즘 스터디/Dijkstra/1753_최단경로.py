import sys
sys.stdin = open('input.txt')

import heapq


def dijkstra():
    que = []
    heapq.heappush(que, [0, k]) # 시작지점 넣기 [가중치 0, 시작 정점 번호 K]
    dist[k] = 0 # 시작지점 길이 0으로 초기화

    while que:
        d, now = heapq.heappop(que) # 가중치와 정점 꺼내기

        if dist[now] < d:   # 저장된 값보다 꺼낸 가중치(값)이 더 크다면 그냥 pass
            continue

        for v in visited[now]:  # 현 정점에서 갈 수 있는 정점 가보기
            nd = v[1] + d   # 현 정점까지의 가중치 더해주기

            if nd < dist[v[0]]: # 저장되어 있는 가중치보다 작다면(최단경로라면)
                dist[v[0]] = nd # 갱신
                heapq.heappush(que, [nd, v[0]]) # 현 정점으로 가보기위해 넣기


v, e = map(int, input().split())    # 정점 개수 v, 간선의 개수 e
k = int(input())    # 시작 정점의 번호 k
dist = [float('INF') for _ in range(v+1)]

visited = [[] for _ in range(v+1)]  # 인접리스트 만들기
for i in range(e):
    u, v, w = map(int, input().split()) # u에서 v로 가는 가중치 w
    visited[u].append([v, w])

dijkstra()

# i번 정점으로의 최단 경로의 경로값 출력
for i in dist[1:]:
    if i == float('INF'):
        print('INF')
    else:
        print(i)
