import sys
sys.stdin = open('input.txt')

n = int(input())    # 도시의 수
cost = [list(map(int, input().split())) for _ in range(n)]  # 비용 행렬
visited = [False for _ in range(n)] # 도시 방문 리스트 (모든 도시를 방문해야 함)
answer = 1e9    # 최소 비용이므로 정답 크게크게

def dfs(s, now, total):
    global answer

    if answer < total:  # 가지치기
        return          # 이미 비용이 기존에 저장한 순회 경로 비용보다 커졌다면 돌아가

    if s == now and False not in visited:   # 모든 도시를 방문했고, 시작지점으로 돌아왔다면
        if total < answer:  # 최소 비용으로 갱신
            answer = total
        return

    for i in range(n):
        if not cost[now][i]:    # 해당 도시로 갈 수 없는 경우 제외
            continue

        if visited[i]:  # 이미 방문한 도시라면 제외
            continue

        visited[i] = True   # 해당 도시 방문처리
        dfs(s, i, total + cost[now][i]) # 다음 도시 가보기 및 비용 더하기
        visited[i] = False  # 방문처리 해제

dfs(0, 0, 0)
print(answer)