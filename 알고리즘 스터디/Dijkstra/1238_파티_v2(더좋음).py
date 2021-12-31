import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra(s, e):
    dist = [float('inf') for _ in range(n+1)]   # 경로 시간 초기화
    queue = []
    heapq.heappush(queue, [0, s])   # 시작 지점 넣어주기
    dist[s] = 0 # 시작지점의 길이 0으로 설정 (시작 -> 시작 의 시간은 0)
    while queue:
        d, now = heapq.heappop(queue)   # 현재까지의 시간과 현재 마을 꺼내기

        if now == e:    # 도착지점이면 시작 -> 현재 마을까지 최단 거리 return
            return d    # 학생 마을 -> x 로 갈때만 해당

        if dist[now] < d:   # 현재 마을까지 걸리는 저장된 시간보다 꺼낸 시간이 더 크다면 pass
            continue

        for next in visited[now]:   # 현재 마을에서 갈 수 있는 곳들 방문
            nd = next[1] + d    # 시간 더하기

            if nd < dist[next[0]]:  # 저장되어있는 시간보다 더 작다면 (더 최단경로가 있다면)
                dist[next[0]] = nd  # 갱신
                heapq.heappush(queue, [nd, next[0]])    # 그 마을 가기
    return dist # x에서 각 마을로 돌아갈때 시간 list로 리턴

n, m, x = map(int, input().split()) # n명 학생, m개의 단방향 도로, x 마을 (파티지점)

visited = [[] for _ in range(n+1)]  # 연결되어 있는 마을 만들기 (인접리스트)
for _ in range(m):
    s, e, t = map(int, input().split()) # 도로 시작점 s, 끝점 e, 필요한 소요시간 t
    visited[s].append([e, t])   # 단방향

x_to_s = dijkstra(x, 0) # 에서 각 학생들의 마을까지 최단시간 구하기

answer = 0
for i in range(1, n+1):
    distance = dijkstra(i, x) + x_to_s[i]   # 왕복 길이
    answer = max(answer, distance)  # 오래 걸리는 학생의 소요시간 갱신

print(answer)
