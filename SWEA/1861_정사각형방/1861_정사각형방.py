import sys
sys.stdin = open('input.txt')

############## DFS ##################

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x, room, cnt):
    global move

    move = max(move, cnt)   # 이동 갱신

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]  # 범위 내에 있고 지금 방보다 1크다면
        if 0 <= ny < n and 0 <= nx < n and room+1 == rooms[ny][nx]:
            dfs(ny, nx, rooms[ny][nx], cnt+1) # 해당 방으로 이동


tc = int(input())
for idx in range(1, tc+1):
    n = int(input())
    rooms = [list(map(int, input().split())) for _ in range(n)]

    max_move = 0             # 최대 이동 횟수
    room_num = 9999999999    # 최대 이동 했을 때의 시작 방 번호
    for i in range(n):
        for j in range(n):
            move = 0    # room[i][j]에서 이동할 수 있는 횟수
            dfs(i, j, rooms[i][j], 1)
            if max_move < move: # 저장되어 있는 최대 이동 횟수보다 더 많이 이동한 경우 정보 갱신
                room_num = rooms[i][j]
                max_move = move
            elif max_move == move:  # 저장되어 있는 최대 이동 횟수와 이동 횟수가 같다면 방 번호 더 작은걸로 갱신
                room_num = min(room_num, rooms[i][j])

    print('#{} {} {}'.format(idx, room_num, max_move))

