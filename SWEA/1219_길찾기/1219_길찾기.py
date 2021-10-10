import sys
sys.stdin = open('input.txt')

def dfs(s):
    global answer
    visited[s] = 1      # 현재 노드 방문 처리
    for i in arr[s]:
        if i == 99:     # 목표 노드 99까지 도달했으면 answer = 1
            answer = 1
        if answer:      # 이미 목표 노드 도달했으면 재귀 들어가지마
            return
        if not visited[i]:  # 목표노드 가는 중이고, 방문한 곳 아니라면 재귀
            dfs(i)


for idx in range(1, 11):
    # 테스트 케이스 순서 idx, 순서쌍의 개수 n
    idx, n = map(int, input().split())
    # 순서쌍 리스트
    pair_list = list(map(int, input().split()))

    arr = [[] for _ in range(100)]

    # 노드 d에 해당하는 리스트(arr[d])에 갈 수 있는 노드 a를 추가한다.
    for d, a in zip(pair_list[:-1:2], pair_list[1::2]):
        arr[d].append(a)

    visited = [0 for _ in range(100)]    # 방문표시
    answer = 0                          # 99까지 갈 수 있나요?

    dfs(0)

    print('#{} {}'.format(idx, answer))
