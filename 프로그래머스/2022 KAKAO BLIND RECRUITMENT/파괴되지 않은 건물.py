def solution(board, skill):
    answer = 0
    h = len(board)
    w = len(board[0])
    temp = [[0 for _ in range(w)] for _ in range(h)]

    for [t, r1, c1, r2, c2, d] in skill:
        if t == 1:
            temp[r1][c1] -= d
            if r2 + 1 < h and c2 + 1 < w:
                temp[r2 + 1][c2 + 1] -= d
            if r2 + 1 < h:
                temp[r2 + 1][c1] += d
            if c2 + 1 < w:
                temp[r1][c2 + 1] += d
        else:
            temp[r1][c1] += d
            if r2 + 1 < h and c2 + 1 < w:
                temp[r2 + 1][c2 + 1] += d
            if r2 + 1 < h:
                temp[r2 + 1][c1] -= d
            if c2 + 1 < w:
                temp[r1][c2 + 1] -= d

    for i in range(h):
        for j in range(1, w):
            temp[i][j] += temp[i][j - 1]

    for j in range(w):
        for i in range(1, h):
            temp[i][j] += temp[i - 1][j]

    for i in range(h):
        for j in range(w):
            board[i][j] += temp[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer