import sys
sys.stdin = open('sample_input.txt')


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def recur(cnt, y, x, num):
    global numbers

    if cnt == 7:    # 여섯번 이동했다면
        numbers.add(num)    # 리스트에 더해
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < 4 and 0 <= ny < 4: # 범위내에 있다면
            recur(cnt+1, ny, nx, num+board[ny][nx]) # 들어가봐


tc = int(input())
for idx in range(1, tc+1):
    board = [list(input().split()) for _ in range(4)]

    numbers = set() # set으로 중복 방지

    # 임의의 위치에서 시작
    for i in range(4):
        for j in range(4):
            recur(0, i, j, '')

    print('#{} {}'.format(idx, len(numbers)))