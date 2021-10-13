import sys
sys.stdin = open('sample_input.txt')


def dfs(node, cnt):
    global answer

    if answer < cnt:    # 더 많은 경로 갔다면 갱신
        answer = cnt

    for next in adj[node]:  # node와 연결된 노드 중에
        if visited[next]:   # 방문한적 있다면 패스
            continue
        visited[node] = True    # 방문처리
        dfs(next, cnt+1)        # 다음노드로 가
        visited[next] = False   # 방문처리 해제


tc = int(input())
for idx in range(1, tc+1):
    n, m = map(int, input().split())

    adj = [[] for _ in range(n+1)]  # 인접 리스트
    for _ in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)    # 무향 그래프
        adj[y].append(x)

    visited = [False for _ in range(n+1)]
    answer = 0  # 최장거리 담을 정답 변수
    for i in range(1, n+1): # 시작 노드를 정하기 위해 for문 돈다
        visited[i] = True   # 시작 노드 방문처리
        dfs(i, 1)   # i 시작 노드도 1개로 세기 때문에 cnt는 1부터 시작한다.
        visited[i] = False  # 해제

    print('#{} {}'.format(idx, answer))