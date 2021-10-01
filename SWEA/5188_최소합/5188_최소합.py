import sys
sys.stdin = open('sample_input.txt')

# 방향 벡터
dx = [1, 0]
dy = [0, 1]

# 오른쪽 아래까지 이동하는 함수 !
def gogo(x, y, total):
    global answer

    if answer < total:  # 이미 합이 크다면 가볼 필요 없어
        return

    if x == y == n-1:   # 오른쪽 아래까지 왔다면
        if total < answer:  # 지금까지 지나온 길의 합이 answer에 들어있는 값보다 작은 경우 갱신
            answer = total
        return

    for i in range(2):  # 오른쪽, 아래 이동
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= n-1 and ny <= n-1: # 주어진 범위 안에 있어야해
            gogo(nx, ny, total+arr[ny][nx]) # 그렇다면 이동해봐 !


tc = int(input())
for idx in range(1, tc+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    answer = 99999999   # 정답 초기화
    gogo(0, 0, arr[0][0])
    print('#{} {}'.format(idx, answer))
