import sys
sys.stdin = open('input.txt')

from collections import deque

# 유사도 k 이상의 비디오 몇개인지 판별하기
def bfs(k, v):
    visited = [0 for _ in range(n+1)]
    visited[v] = True
    queue = deque([(v, 999999999999999)])
    cnt = 0
    while queue:
        now, usado = queue.popleft()    # 현재 비디오, 최소 유사도

        for nxt_v, nxt_u in graph[now]:
            # 존은 두 쌍 사이의 동영상의 유사도를 그 경로의 모든 연결들의 유사도 중 최솟값으로 하기로 함
            # 따라서 현재까지의 최소 유사도와 현재 비디오와 다음 비디오의 유사도 중 최솟값으로 갱신
            nxt_u = min(usado, nxt_u)
            # 방문하지 않은 곳이고, 유사도가 k이상이라면
            if not visited[nxt_v] and k <= nxt_u:
                queue.append((nxt_v, nxt_u))
                cnt += 1
                visited[nxt_v] = True
    return cnt


n, q = map(int, input().split())
# 동영상 인접 리스트 만들기
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    v1, v2, usado = map(int, input().split())
    graph[v1].append((v2, usado))
    graph[v2].append((v1, usado))

# 농부 존의 q개 질문
for _ in range(q):
    k, v = map(int, input().split())
    print(bfs(k, v))