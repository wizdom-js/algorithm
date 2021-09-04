import sys
sys.stdin = open('input.txt')

def go(board, loc):
    global result
    while True:
        locx = loc[0] + dx[k]
        locy = loc[1] + dy[k]
        if board[locx][locy] == '#' or board[locx][locy] == 'R' or board[locx][locy] == 'B':
            break
        elif board[locx][locy] == 'O':
            result = True
            break
        else:
            loc = [locx, locy]
    return loc

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            r = [i, j]
        if board[i][j] == 'B':
            b = [i, j]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
k = 0
k_cnt = [0, 0, 0, 0]
cnt = 0
result = False
r_result = False
b_result = False
direct = -1
r_list = [r]

while True:
    if k_cnt[k] == 1:
        k = (k + 1) % 4
        pass
    else:
        rx = r[0] + dx[k]
        ry = r[1] + dy[k]
        if board[rx][ry] == '.':
            board[r[0]][r[1]] = '.'
            r = go(board, r)
            if r in r_list:
                cnt = -1
                break
            else:
                r_list.append(r)
            board[r[0]][r[1]] = 'R'
            direct = (k+2)%4
            k_cnt = [0, 0, 0, 0]
            k_cnt[direct] = 1
            cnt += 1
            if result:
                board[r[0]][r[1]] = '.'
                r_result = True
                result = False
            bx = b[0] + dx[k]
            by = b[1] + dy[k]
            if board[bx][by] == '.':
                board[b[0]][b[1]] = '.'
                b = go(board, b)
                board[b[0]][b[1]] = 'B'
                if result:
                    b_result = True
            else:
                if r_result:
                    break

            if r_result == True and b_result == True:
                cnt = -1
                break
            elif r_result == True and b_result == False:
                break
            elif r_result == False and b_result == True:
                cnt = -1
                break

        elif board[rx][ry] == 'O':
            cnt += 1
            break
        else:
            k_cnt[k] = 1
            k = (k + 1) % 4
            if k_cnt.count(0) == 0:
                k_cnt = [0, 0, 0, 0]
                k_cnt[(direct+2)%4] = 1
                r = r_list[-2]

print(cnt)
