import sys
sys.stdin = open('input.txt')

import heapq

def dikstra(s, e):
    dist = [float('inf') for _ in range(n + 1)] # 초기화

    queue = []
    heapq.heappush(queue, [0, s])   # 시작 지점 넣기
    dist[s] = 0
    while queue:
        d, now = heapq.heappop(queue)   # 거리, 현재 정점

        if now == e:    # 도착 정점이면 중단
            break

        if dist[now] < d:   # 가지치기
            continue

        for next in visited[now]:   # 현재 정점에서 갈 수 있는 정점 탐방
            nd = next[1] + d        # 거리 더해주기
            if nd < dist[next[0]]:  # 출발 정점 ~ 다음 정점까지의 거리보다 작다면
                dist[next[0]] = nd  # 업데이트
                heapq.heappush(queue, [nd, next[0]]) # 정점으로 가보기

    return dist[e]  # 거리 반환


n, e = map(int, input().split()) # 정점의 개수 n, 간선의 개수 e

visited = [[] for _ in range(n+1)]  # 인접리스트 만들기
for i in range(e):
    s, e, l = map(int, input().split()) # 시작 정점, 도착 정점, 거리
    visited[s].append([e, l])   # 양방향
    visited[e].append([s, l])

v1, v2 = map(int, input().split())  # 반드시 거쳐야 하는 두 개의 정점
mid = dikstra(v1, v2)   # v1 <-> v2 거리
answer1 = dikstra(1, v1) + mid + dikstra(v2, n) # 1 -> v1 -> v2 -> n
answer2 = dikstra(1, v2) + mid + dikstra(v1, n) # 1 -> v2 -> v1 -> n

if answer1 == float('inf') and answer2 == float('inf'): # 경로 없을경우
    print(-1)
else:
    print(answer1 if answer1 < answer2 else answer2)    # 더 짧은 거리 반환