import sys
sys.stdin = open('input.txt')

from collections import deque


def dfs(com):
    for nxt_com in graph[com]:
        if not visited[nxt_com]:
            visited[nxt_com] = 1
            trust[nxt_com] += trust[com]
            dfs(nxt_com)
            # visited[nxt_com] = 0


# 해킹할 수 있는 모든 곳 다 가보고 방문처리하기
def bfs(s):
    visited = [0 for _ in range(n+1)]
    visited[s] = True

    queue = deque([s])
    while queue:
        now = queue.popleft()

        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

    # 방문한 곳 => 해킹한 컴퓨터 이므로 방문 개수를 반환
    return sum(visited)


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
# trust = [0 for _ in range(n+1)]
for _ in range(m):
    com1, com2 = map(int, input().split())
    graph[com2].append(com1)    # com2에서 com1을 감염 시킬(방문 할) 수 있다.
    # trust[com2] += 1

answer = []
max_v = 0
for i in range(1, n+1):
    tmp_v = bfs(i)

    if max_v < tmp_v:   # 해킹할 수 있는 컴퓨터 수가 더 많은 경우
        answer = [i]    # 배열 초기화
        max_v = tmp_v   # 업데이트
    elif max_v == tmp_v:    # 수가 같은 경우에는 추가
        answer.append(i)

print(*answer)


