import sys
sys.stdin = open('sample_input.txt')

# 방향 벡터 / 상, 하, 좌, 우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

# 미로탈출 bfs(시작 y좌표, 시작 x 좌표) -> 2의 위치
def bfs(sy, sx):
    q = [(sy, sx)]  # q에 시작 좌표 넣어주고 시작

    # q가 빌때까지 반복
    while q:
        now_y, now_x = q.pop(0) # 현재 좌표 q에서 가져오기 (bfs니까 맨앞에꺼)
        # 상하좌우 탐색
        for i in range(4):
            # 이동해볼 좌표 설정 (현재 위치 + 방향 벡터가 가리키는 곳)
            next_y = now_y + dy[i]
            next_x = now_x + dx[i]

            # 이동해볼 곳이 미로 범위 안에 있다 ?
            if 0 <= next_y < n and 0 <= next_x < n:
                # 그리고 거기가 방문하지 않았던 곳이고, 통로('0')이다?
                if not visited[next_y][next_x] and maze[next_y][next_x] == '0':
                    q.append((next_y, next_x))      # 그렇담 가보자 q에 넣어놔
                    visited[next_y][next_x] = visited[now_y][now_x] + 1  # 이동해볼 곳이 출발 한 곳으로부터 통로를 몇개나 이동했는지 표시

                # 이동해볼 곳이 출구다 ??????
                elif maze[next_y][next_x] == '3':
                    return visited[now_y][now_x]   # 현재까지 통로 지난 횟수(몇 칸 지나왔는지) 반환 (3까지 거리 X, 0 지난 횟수 O)

    # q 비었는데 출구 못찾았나요? -> 경로 없음
    return 0



tc = int(input())

for idx in range(1, tc+1):
    n = int(input())

    sy = sx = -1    # 시작점 좌표 (sy 행, sx 열)
    maze = []
    for i in range(n):
        maze.append(input())
        # 시작점 좌표 찾기
        # (-1은 2찾은 경우는 and 뒤의 조건 만족하는지 탐색 안하기 위함)
        if sy == -1 and '2' in maze[i]:
            sy = i
            sx = maze[i].find('2')

    # 방문 리스트 & 통로 지난 횟수 계산 리스트
    visited = [[0 for _ in range(n)] for _ in range(n)]

    print('#{} {}'.format(idx, bfs(sy, sx)))

    # visited 출력해서 한눈에 보기
    for i in range(n):
        print(*visited[i])