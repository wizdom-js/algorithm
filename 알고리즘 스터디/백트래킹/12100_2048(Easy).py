import sys
sys.stdin = open('input.txt')


def up2(board):
    for j in range(n):
        i = n
        while 0 < i:
            i -= 1
            if not board[i][j]: continue

            if board[i-1][j] == 0:
                board[i-1][j] = board[i][j]
                board[i][j] = 0
            elif board[i-1][j] == board[i][j]:
                board[i-1][j] += board[i][j]
                board[i][j] = 0

    return board

def up(board):
    new_board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        tmp = 0
        for j in range(n):
            if board[j][i]:
                new_board[tmp][i] = board[j][i]
                for z in range(tmp, 0, -1):
                    if new_board[z-1][i] == new_board[z][i]:
                        new_board[z-1][i] *= 2
                        new_board[z][i] = 0
                        tmp -= 1
                tmp += 1
    return new_board

def down(board):
    new_board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        tmp = n-1
        for j in range(n-1, -1, -1):
            if board[j][i]:
                new_board[tmp][i] = board[j][i]
                for z in range(n-2, tmp-1, -1):
                    if new_board[z+1][i] == new_board[z][i]:
                        new_board[z+1][i] *= 2
                        new_board[z][i] = 0
                        tmp += 1
                tmp -= 1
    return new_board

def left(board):
    new_board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        tmp = 0
        for j in range(n):
            if board[i][j]:
                new_board[i][tmp] = board[i][j]
                for z in range(tmp, 0, -1):
                    if new_board[i][z - 1] == new_board[i][z]:
                        new_board[i][z - 1] *= 2
                        new_board[i][z] = 0
                        tmp -= 1
                tmp += 1

    return new_board

def right(board):
    for i in range(n):
        print(*board[i])
    print('--------------------------------')
    new_board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        tmp = n - 1
        for j in range(n - 1, -1, -1):
            if board[i][j]:
                new_board[i][tmp] = board[i][j]
                for z in range(n - 2, tmp - 1, -1):
                    if new_board[i][z + 1] == new_board[i][z]:
                        new_board[i][z + 1] *= 2
                        new_board[i][z] = 0
                        tmp += 1
                tmp -= 1
    for i in range(n):
        print(*new_board[i])
    print('---------asdfasdfsfadfasdf-----------------------')
    return new_board



def dfs(cnt, board):
    global answer
    if cnt == 5:
        for i in range(n):
            max_block = max(board[i])
            if answer < max_block:
                answer = max_block
        return


    dfs(cnt+1, up(board))
    dfs(cnt+1, down(board))
    dfs(cnt + 1, left(board))
    dfs(cnt + 1, right(board))


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 0
# right(board)
for i in range(n):
    print(*board[i])
dfs(0, board)
print(answer)

'''
3
0 0 0
2 4 8
2 4 8
'''