import sys
sys.stdin = open('input.txt')

from collections import deque

'''
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(sy, sx):
    queue = deque([[sy, sx, 20]])
    while queue:
        y, x, beer = queue.popleft()
        if beer == 0:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 32767 and 0 <= nx < 32767 and not visited[ny][nx]:
                if point[ny][nx] == 'p':
                    visited[ny][nx] = 1
                    queue.append([ny, nx, 20])
                elif point[ny][nx] == 'e':
                    return 'happy'
                else:
                    visited[ny][nx] = 1
                    queue.append([ny, nx, beer-1])
    return 'sad'



tc = int(input())
for tc_n in range(1, tc+1):
    n = int(input())
    point = [[0 for _ in range(400)] for _ in range(400)]
    for i in range(n+2):
        if i == 0:
            sx, sy = map(int, input().split())
            point[sy//50][sx//50] = 's'
        elif i == n+1:
            x, y = map(int, input().split())
            point[y//50][x//50] = 'e'
        else:
            x, y = map(int, input().split())
            point[y//50][x//50] = 'p'

    visited = [[0 for _ in range(400)] for _ in range(400)]

    print(bfs(sy, sx))

'''
####################################################


def bfs(sx, sy):
    queue = deque([(sx, sy)])   # 출발지점 넣기
    visited[(sx, sy)] = False    # 출발지점 방문 처리
    while queue:
        x, y = queue.popleft()  # 좌표 하나 빼
        if abs(ex-x) + abs(ey-y) <= 1000:   # 현재 지점에서 도착지점까지 맥주 20개로 갈 수 있다면
            return 'happy'  # 'happy' 출력

        for i in range(len(cu)):
            cu_x = cu[i][0] # 편의점 가보기
            cu_y = cu[i][1]
            # 현재 편의점에서 목적지까지 맥주 20개로 갈 수 있고 방문해본 편의점이 아니라면
            if abs(cu_x-x) + abs(cu_y-y) <= 1000 and visited.get((cu_x, cu_y), True):
                visited[(cu_x, cu_y)] = False   # 방문처리
                queue.append((cu_x, cu_y))      # 방문해보자 queue에 넣어
    return 'sad'    # 출발 그리고 편의점에서도 맥주 20개로 목적지까지 못가면 'sad'


tc = int(input())
for tc_n in range(1, tc+1):
    n = int(input())    # 편의점 개수

    sx, sy = map(int, input().split())  # 출발 좌표
    cu = [] # 편의점 좌표 저장
    for i in range(n):
        cu.append(list(map(int, input().split())))
    ex, ey = map(int, input().split())  # 페스티벌 좌표

    visited = {}

    print(bfs(sx, sy))










'''
3
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000
2
0 0
-450 -250
-600 500
-600 1000
'''