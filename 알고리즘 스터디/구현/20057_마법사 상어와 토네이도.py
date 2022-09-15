import sys
sys.stdin = open('input.txt')

# 모래 이동 비율
ratio = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]

# 모래 이동시키기
def move_sand():
    y, x = tornado[0], tornado[1]
    sand_amount = board[tornado[0]][tornado[1]]
    out_sand = 0
    left_sand = sand_amount

    # 비율대로 모래 이동시키기
    for i in range(5):
        for j in range(5):
            if ratio[i][j]:
                tmp_sand = int(sand_amount * ratio[i][j])
                left_sand -= tmp_sand

                ny, nx = y - 2 + i, x - 2 + j
                if 0 <= ny < n and 0 <= nx < n: # 모래가 격자 안에 있는 경우
                    board[ny][nx] += tmp_sand
                else:                           # 격자 밖으로 나간 경우
                    out_sand += tmp_sand

    # 남은 모래 알파로 이동시키기
    ny, nx = y + dy, x + dx
    if 0 <= ny < n and 0 <= nx < n:
        board[ny][nx] += left_sand
    else:
        out_sand += left_sand

    return out_sand


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

move = 0
direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # 토네이도 이동 방향 [y, x] => 상, 좌, 상, 우 (시작은 좌부터)
tornado = [n//2, n//2]  # 토네이도 시작 중간지점
answer = 0

go = 1
while tornado[1] != -1:
    if go % 2:  # 토네이도 두번 방향 바꾸었다면 이동거리 한칸 늘어남
        move += 1

    dy, dx = direction[go % 4][0], direction[go % 4][1] # 다음 이동 방향
    # 이동 거리 만큼 직진하기
    for m in range(move):
        tornado[0] += dy
        tornado[1] += dx
        answer += move_sand()
        board[tornado[0]][tornado[1]] = 0

    # 모래 퍼지는 비율 -90도로 전환 
    ratio = list(reversed(list(zip(*ratio))))

    go += 1

print(answer)





