def delete_blocks(m, n, board, cnt):
    del_blocks = set()
    for i in range(n - 1):
        for j in range(m - 1):
            block = board[i][j]
            if block == 0:
                continue
            if block == board[i][j + 1] and block == board[i + 1][j] and block == board[i + 1][j + 1]:
                del_blocks.update([[i, j], [i, j + 1], [i + 1, j], [i + 1, j + 1]])

    if del_blocks:
        for i, j in list(del_blocks):
            del board[i][j]
            board[i].append(0)
            cnt += 1
        return cnt
    else:
        return False


def solution(m, n, board):
    board = list(map(list, zip(*board)))

    cnt = 0
    while True:
        temp = delete_blocks(m, n, board, cnt)
        print(board)
        if temp:
            cnt += temp
        else:
            return cnt