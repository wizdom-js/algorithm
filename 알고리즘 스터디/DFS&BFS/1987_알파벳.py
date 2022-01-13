import sys
sys.stdin = open('input.txt')

from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

# 메모리 초과
def bfs():
    queue = deque([[0, 0, 1, board[0][0]]])
    while queue:
        y, x, cnt, alphabets = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h and 0 <= nx < w and board[ny][nx] not in alphabets:
                queue.append([ny, nx, cnt+1, alphabets+board[ny][nx]])
    return cnt

def dfs(y, x, cnt):
    global answer
    if answer < cnt:
        answer = cnt

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < h and 0 <= nx < w:
            if not alphabet[ord(board[ny][nx])]:
                alphabet[ord(board[ny][nx])] = True
                dfs(ny, nx, cnt + 1)
                alphabet[ord(board[ny][nx])] = False

def dfs_bit(y, x, cnt, visit):
    global answer
    if answer < cnt:
        answer = cnt

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < h and 0 <= nx < w:
            bit = 1 << (ord(board[ny][nx]) - 60)
            if visit & bit:
                continue
            dfs_bit(ny, nx, cnt + 1, visit|bit)
            # visit &= ~bit


h, w = map(int, input().split())    # 세로 h, 가로 w
board = [list(input()) for _ in range(h)]
alphabet = [False for _ in range(150)]

# print(bfs)

# answer = 0
# alphabet[ord(board[0][0])] = True
# dfs(0, 0, 1)

answer = 0
visit = 0
visit |= (1 << (ord(board[0][0]) - 60))
dfs_bit(0, 0, 1, visit)
print(answer)
