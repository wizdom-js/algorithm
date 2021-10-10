import sys
sys.stdin = open("sample_input.txt")

###### 백트래킹 #######

# 델타 방향 탐색 (상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 탈출 함수
def escape(sy, sx):
    global result

    # 현재 위치 표시 (지나왔다고 표시하기 다시 탐색 안하도록)
    maze[sy][sx] = 2

    # 이미 출구 찾았으면 돌아가
    if result:
        return

    # 방향 잡기
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]

        # 미로 안에서만 탐색하도록 조건문 설정
        if 0 <= ny < n and 0 <= nx < n:
            # 가고자 하는 곳이 도착지점이면 result = 1
            if maze[ny][nx] == 3:
                result = 1
                return
            # 가고자 하는 곳이 통로이면 들어가기
            if maze[ny][nx] == 0:
                escape(ny, nx)


tc = int(input())

for idx in range(1, tc+1):
    n = int(input())

    # 미로 받아오기 & 출발 지점 찾기
    maze = []
    sx = 0
    for i in range(n):
        maze.append(list(map(int, input())))
        # 2아직 못찾았고, 받아온 리스트에 출발지점이 있으면 출발 지점 저장
        if not sx and 2 in maze[i]:
            sy = i
            sx = maze[i].index(2)

    result = 0      # 결과의 기본값 0으로 준다.

    escape(sy, sx)  # 탈출 함수
    print('#{} {}'.format(idx, result))