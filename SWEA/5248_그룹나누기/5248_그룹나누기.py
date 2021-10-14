import sys
sys.stdin = open('sample_input.txt')


def dfs(now):
    for nxt in adj[now]:
        if visited[nxt]:
            continue
        visited[nxt] = True # 팀 배정 완료해
        dfs(nxt)    # 또 같은 팀 누군지 봐


tc = int(input())
for idx in range(1, tc+1):
    n, m = map(int, input().split())    # 출석번호 n, 신청서 m
    numbers = list(map(int, input().split()))

    adj = [[] for _ in range(n+1)]  # 인접 리스트 만들기
    for i in range(0, m*2, 2):
        adj[numbers[i]].append(numbers[i+1])
        adj[numbers[i+1]].append(numbers[i])    # 시작 노드보다 부모 노드가 있을 수 있기 때문에 방향 없는 리스트로 만들어줌

    answer = 0
    visited = [False for _ in range(n+1)]   # 방문 처리 리스트
    for i in range(1, n+1): # 노드 쫙 돌면서
        if not visited[i]:  # i 노드 어떤 팀에 속해있지 않다면
            visited[i] = True   # 방문처리로 팀 배정 완료
            dfs(i)  # 같은 팀 누군지 봐
            answer += 1 # 팀 개수 +1

    print('#{} {}'.format(idx, answer))



