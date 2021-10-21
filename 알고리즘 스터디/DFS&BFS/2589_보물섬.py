import sys
sys.stdin = open('input.txt')

from collections import deque

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(sy, sx, hour):
    queue = deque([(sy, sx, hour)]) # 시작지점 추가하고 시작
    visited = [[0 for _ in range(garo)] for _ in range(sero)]   # 방문한 곳 다시 방문하지 못하도록 만든 리스트
    visited[sy][sx] = 1  # 시작지점 방문처리
    while queue:
        y, x, hour = queue.popleft()    # 좌표 하나 가져오기
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < sero and 0 <= nx < garo:   # 다음 갈 곳이 지도 범위를 벗어나지 않는다면
                if treasure_map[ny][nx] == 'W' or visited[ny][nx]:  # 다음 갈 곳이 바다이거나 방문했던 곳이면 가지않도록
                    continue
                visited[ny][nx] = 1 # 방문처리
                queue.append((ny, nx, hour+1))  # queue에 가볼 곳으로 추가하기
    return hour # 시작지점에서 막다른 곳까지 걸리는 시간 return


sero, garo = map(int, input().split())          # 지도의 세로 길이, 가로 길이
treasure_map = [input() for _ in range(sero)]   # 보물 지도

answer = 0
for h in range(sero):
    gap = 0
    for w in range(garo):
        if gap:
            gap -= 1
            continue
        if treasure_map[h][w] == 'L':   # 해당 좌표 육지이면
            tmp = bfs(h, w, 0)
            if answer < tmp:  # 탐색해보는데, 더 긴 시간으로 갱신
                answer = tmp
            else:
                gap = answer - tmp
print(answer)