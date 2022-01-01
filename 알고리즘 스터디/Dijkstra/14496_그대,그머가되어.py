import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra():
    dist = [float('inf') for _ in range(n+1)]   # 가중치 초기화
    queue = [[0, a]]    # 횟수, 시작 문자 넣기
    dist[a] = 0     # 시작지점 가중치 0
    while queue:
        d, now = heapq.heappop(queue)   # 현재까지 치환 횟수, 현재 문자 뽑기

        if now == b:    # 바꾸려고 하는 문자 b라면
            print(d)    # 현재까지 치환 횟수 출력
            return

        if dist[now] < d:   # 저장한 치환횟수보다 꺼낸게 더 크다면 패스
            continue

        for next in visited[now]:   # 현재 문자에서 바꿀 수 있는 문자로 가보기
            nd = d + 1  # 치환 횟수 + 1
            if nd < dist[next]: # 저장한 치환 횟수보다 적다면 갱신
                dist[next] = nd
                heapq.heappush(queue, [nd, next])   # 해당 문자로 가보기

    print(-1)   # 문자 b로 바꿀 수 없다면 -1 출력
    return


a, b = map(int, input().split())    # 바꾸려고 하는 문자 a, b
n, m = map(int, input().split())    # 전체 문자의 수 n, 치환 가능한 문자쌍의 수 m

visited = [[] for _ in range(n+1)]  # 인접 리스트 만들기
for _ in range(m):
    t1, t2 = map(int, input().split())  # 바꿀 수 있는 두 문자
    visited[t1].append(t2)  # 양방향 
    visited[t2].append(t1)

dijkstra()