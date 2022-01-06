import sys
sys.stdin = open('input.txt')

import copy

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


h, w = map(int, input().split())    # 보드의 세로 h, 가로 w 크기
board = [[] for _ in range(h)]
answer = 99

ry = rx = by = bx = -1 # 빨간 구슬, 파란 구슬 좌표
for i in range(h):
    board[i] = list(input())

    # 빨간 구슬 위치 찾기
    if ry == -1 and 'R' in board[i]:
        ry = i
        rx = board[i].index('R')
    # 파란 구슬 위치 찾기
    if by == -1 and 'B' in board[i]:
        by = i
        bx = board[i].index('B')


def where(ry, rx, by, bx, cnt, j, old_board):
    global answer

    if 10 < cnt:
        return

    for i in range(4):
        if j == i : continue
        nry, nrx = ry + dy[i], rx + dx[i]
        nby, nbx = by + dy[i], bx + dx[i]
        board = copy.deepcopy(old_board)
        if board[nry][nrx] == '#':
            continue
        elif board[nry][nrx] == 'B' and board[nby][nbx] != '#':
            board[by][bx] = '.'
            by, bx = go(nby, nbx, i, 'B', board)
            board[ry][rx] = '.'
            ry, rx = go(nry, nrx, i, 'R', board)
        elif board[nry][nrx] == 'O':
            answer = min(answer, cnt)
            return
        else:
            board[ry][rx] = '.'
            ry, rx = go(nry, nrx, i, 'R', board)
            if board[nby][nbx] == '#': continue
            board[by][bx] = '.'
            by, bx = go(nby, nbx, i, 'B', board)

        if ry == 'ok':
            answer = min(answer, cnt)
            return
        print('-----------', i, '-----------------')

        for i in range(h):
            print(*board[i])

        where(ry, rx, by, bx, cnt+1, i, board)
    if by == 'ok' and ry != 'ok':
        answer = -1
        return
    print('################################')


def go(y, x, d, bead, board):
    global h, w
    board[y][x] = bead

    while True:
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < h and 0 <= nx < w:
            if board[ny][nx] == 'O':
                board[y][x] = '.'
                return 'ok', 'ok'
            elif board[ny][nx] == '.':
                board[y][x] = '.'
                board[ny][nx] = bead
                y, x = ny, nx
            else:
                return y, x


where(ry, rx, by, bx, 1, -1, board)
print(answer)
