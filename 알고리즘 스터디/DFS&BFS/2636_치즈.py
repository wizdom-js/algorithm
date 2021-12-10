import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    visited = [[False for _ in range(w)] for _ in range(h)] # 방문처리 배열
    queue = deque([(0, 0)]) # 처음 위치 0,0
    melted = 0              # 녹인 치즈 개수
    while queue:
        y, x = queue.popleft()  # 이동할 곳 가져오기
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < h and 0 <= nx < w: # 움직일 곳이 범위 내라면
                if cheese[ny][nx] == 0 and not visited[ny][nx]: # 판(0)이고, 방문하지 않은 곳이라면
                    visited[ny][nx] = True  # 방문처리
                    queue.append((ny, nx))  # 해당 위치에서 검토해보기 위해 queue에 넣어줌 (판에서 만난 치즈는 다 가장자리 치즈이므로)
                elif cheese[ny][nx] == 1:   # 가장자리 치즈라면
                    cheese[ny][nx] = 0      # 녹이기
                    melted += 1
                    visited[ny][nx] = True
    return melted   # 녹인 치즈 개수 반환


h, w = map(int, input().split())    # 치즈판의 높이와 너비
cheese = [list(map(int, input().split())) for _ in range(h)]    # 받아온 치즈 판

time = 0    # 모든 치즈를 녹이는데 걸린 시간
mc = 0      # 1시간마다 녹은 치즈 개수를 저장할 변수 (1시간 전 치즈 개수 반환해야하므로)
while True:
    tmp = bfs()     # 치즈 녹이기
    if tmp == 0:    # 만약 녹일 치즈가 없다면 끝내기
        break
    mc = tmp        # 녹은 치즈 있었다면 개수 저장해놓기
    time += 1       # 시간 + 1

print(time)
print(mc)