import sys
sys.stdin = open('input.txt')


dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x):
    visited[y][x] = True
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
            if grid[ny][nx] == grid[y][x]:  # 같은 색이면 탐색
                dfs(ny, nx)


n = int(input()) # 그리드 칸 n x n
grid = [list(input()) for _ in range(n)]   # 그리드

not_cw = cw = 0 # 적녹색약이 아닌 사람이 봤을때의 구역의 수, 적녹색약인 사람이 봤을 때의 구역의 수

# 적녹색약이 아닌 사람이 봤을 때
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:   # 아직 방문안한 구역이라면
            dfs(i, j)   # 탐색
            not_cw += 1 # 구역 수  + 1

# 적녹색약인 사람이 봤을 때
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'G':   # 적녹색 차이를 거의 느끼지 못하기 때문에 통일 시켜주기
            grid[i][j] = 'R'


visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            cw += 1

print(not_cw, cw)
