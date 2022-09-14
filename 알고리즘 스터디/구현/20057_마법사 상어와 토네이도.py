import sys
sys.stdin = open('input.txt')

ratio = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]


def move_sand():
    y, x = tornado[0], tornado[1]
    sand_amount = board[tornado[0]][tornado[1]]
    out_sand = 0
    left_sand = sand_amount
    for i in range(5):
        for j in range(5):
            if ratio[i][j]:
                tmp_sand = int(sand_amount * ratio[i][j])
                left_sand -= tmp_sand
                ny, nx = y - 2 + i, x - 2 + j
                if 0 <= ny < n and 0 <= nx < n:
                    board[ny][nx] += tmp_sand
                else:
                    out_sand += tmp_sand

    rotate_ratio = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(n):
        for j in range(n):
            rotate_ratio[i][j] = board[j][n-1-i]

    return left_sand


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

move = 0
direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
tornado = [n//2, n//2]
answer = 0

for i in range(1, n*2):
    if i % 2:
        move += 1

    print(tornado)
    answer += move_sand()



    tornado = [tornado[0] + move * direction[i % 4][0], tornado[1] + move * direction[i % 4][1]]

print(answer)

for i in range(n):
    print(*board[i])




