import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 최단 경로 => bfs
def bfs(s):
    visited = [[0 for _ in range(w)] for _ in range(h)]
    mineral_cnt = 0

    queue = deque()
    # 입력받은 채굴기 강도로 시작할 수 있는 곳 다 queue에 넣기
    for y, x in start_point:
        if mine[y][x] <= s:
            visited[y][x] = True
            queue.append([y, x])

    while queue:
        y, x = queue.popleft()

        mineral_cnt += 1    # 큐에 들어갔다 나옴 => 채굴기 강도(s)로 캘 수 있는 광물
        if mineral_cnt == min_mineral:  # 최소 광물 수 만족하면 중단
            return True

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx]:
                if mine[ny][nx] > s:    # 채굴기 강도로 캘 수 없는 경우
                    continue
                visited[ny][nx] = True
                queue.append([ny, nx])

    return False


h, w, min_mineral = map(int, input().split())   # 광산 세로, 가로, 캐야하는 최소 광물의 수

mine = []   # 광산
start_point = []

for i in range(h):
    tmp = list(map(int, input().split()))
    mine.append(tmp)

    # 시작 지점 추가해주기
    if i > 0:
        start_point.append([i, 0])
        start_point.append([i, w-1])
    else:
        for j in range(w):
            start_point.append([0, j])

min_s = 1
max_s = 10**6

# 최소 채굴기 강도 찾기 위한 이분탐색
while min_s <= max_s:
    mid_s = (min_s + max_s) // 2
    if bfs(mid_s):  # 해당 채굴기 강도로 광물 수만큼 캘 수 있다면
        max_s = mid_s - 1
    else:   # 캘 수 없는 경우
        min_s = mid_s + 1

print(min_s)
