import sys
sys.stdin = open('sample_input.txt')

# 다시 확인
######### 재귀 버전 #########

def dfs(s):

    # 현재 노드 방문 처리
    visited[s] = 1

    # if s == g:
    #     print(g)
    #     return

    # 노드 개수 만큼 반복
    for i in range(1, v + 1):
        # 현재노드에서 다음 노드로 갈 수 있고 (arr[s][i] == 1)
        # 방문하지 않았던 곳이라면
        if arr[s][i] and visited[i] == 0:
            # 목표 도착 노드가 아닌 경우
            dfs(i)



t = int(input())

for idx in range(1, t+1):
    # 노드 개수 v, 간선개수 e
    v, e = map(int, input().split())
    # 인접행렬 만들기 (인덱스 사용 편하게 하기 위해 range(v+1) 해주었음)
    arr = [[0 for _ in range(v+1)] for _ in range(v+1)]

    # 인접행렬에 방향성 표시하기
    for _ in range(e):
        # 출발노드 d, 도착 노드 a
        d, a = map(int, input().split())
        arr[d][a] = 1   # 한방향이므로 반대로도 설정해주면 (arr[a][d] == 1) 안됨

    # 경로 존재 확인할 출발 노드 s, 도착 노드 g
    s, g = map(int, input().split())
    visited = [0 for _ in range(v + 1)]  # 방문 표시

    dfs(s)

    print('#{} {}'.format(idx, visited[g]))