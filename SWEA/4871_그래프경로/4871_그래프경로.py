import sys
sys.stdin = open('sample_input.txt')

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

    stack = []                          # 방문 경로 저장할 리스트
    visited = [0 for _ in range(v+1)]   # 방문 표시
    visited[s] = 1                      # 시작노드 방문 표시
    answer = 0                          # 도착노드에 갈 수 있는지, 없는지
    road = [s]                          # 경로

    while answer == 0:
        # 노드 개수 만큼 반복
        for i in range(1, v+1):
            # 현재노드에서 다음 노드로 갈 수 있고 (arr[s][i] == 1)
            # 방문하지 않았던 곳이라면
            if arr[s][i] and visited[i] == 0:

                # 목표 도착 노드에 도달 했을 경우
                if i == g:
                    answer = 1
                    road.append(g)
                    break

                # 목표 도착 노드가 아닌 경우
                else:
                    stack.append(s)     # 방문 경로 저장
                    s = i               # 다음 노드로 이동
                    visited[i] = 1      # 이동한 노드 방문 표시
                    road.append(i)
                    break

        # 현재 노드에서 다음 노드로 갈 수 있는 곳이 없거나
        # 혹은 이미 방문한 곳이었다면
        else:
            if stack:             # 이전 노드 다시 탐색
                s = stack.pop()
                road.pop()
            else:                 # 탐색할 노드도 없다면 while문 중단
                break

    print('#{} {}'.format(idx, answer))
    print('road=', *road)