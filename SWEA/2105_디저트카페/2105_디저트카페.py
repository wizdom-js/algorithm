import sys
sys.stdin = open('sample_input.txt')

dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]

def dfs(y, x, s, cnt, dessert):
    global answer

    for i in range(s, 4):   # 사각형 모향의 방향은 오직 네가지만 나온다. 따라서 이전에 갔던 방향은 고려하지 않는다.
        ny = y + dy[i]  # 다음 대각선
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and visited[ny][nx]: # 다음에 갈 곳이 범위 안에 있고 방문한 곳이 아니면
            if cafe[ny][nx] in dessert: # 만약 같은 숫자의 디저트 파는 곳이라면 ?
                if visited[ny][nx] == 2:   # 근데 그게 출발지이고, 최소 4곳 다녀왔다면 ?
                    answer = max(answer, cnt)   # 더 많은 디저트 수로 갱신
                    return
                continue    # 출발지 아니고 그냥 겹치는 경우라면 넘어가도록

            visited[ny][nx] = 0 # 방문 처리
            dfs(ny, nx, i, cnt+1, dessert + [cafe[ny][nx]]) # 다음 갈 곳 들어가봐
            visited[ny][nx] = 1 # 다음 사용을 위해 방문처리 해제


tc = int(input())
for idx in range(1, tc+1):
    n = int(input())    # 행 한줄에 있는 카페 개수
    cafe = [list(map(int, input().split())) for _ in range(n)]  # 디저트 카페
    visited = [[1 for _ in range(n)] for _ in range(n)] # 방문처리할 배열

    answer = -1
    for i in range(n):
        for j in range(1, n):
            visited[i][j] = 2   # 출발지 표시
            dfs(i, j, 0, 1, [cafe[i][j]])   # 탐색 고고
            visited[i][j] = 1   # 다음 탐색을 위해 출발지 리셋

    print('#{} {}'.format(idx, answer))