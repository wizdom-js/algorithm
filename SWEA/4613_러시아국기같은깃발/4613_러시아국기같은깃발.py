import sys
sys.stdin = open('sample_input.txt')


def paint(before, cnt, i):
    global answer

    if answer < cnt:
        return

    i += 1

    if i == n - 1:
        if cnt < answer:
            answer = cnt
        return

    if before == 'W':
        if i != n-2:
            paint('W', cnt + board[i][0], i)
        paint('B', cnt + board[i][1], i)

    elif before == 'B':
        paint('B', cnt + board[i][1], i)
        paint('R', cnt + board[i][2], i)

    elif before == 'R':
        paint('R', cnt + board[i][2], i)



tc = int(input())

for idx in range(1, tc+1):
    n, m = map(int, input().split())

    board = []
    for _ in range(n):
        line = input()
        w = m - line.count('W')
        b = m - line.count('B')
        r = m - line.count('R')
        board.append([w, b, r])

    answer = 999999999999

    paint('W', board[0][0]+board[-1][2], 0)

    print('#{} {}'.format(idx, answer))
    print(board)


