import sys
sys.stdin = open('input.txt')


import heapq

# 방향 벡터
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def dijkstra():
    queue = [[rupee[0][0], 0, 0]]  # 탐험 할 곳 담아둘 리스트 # 시작지점 루피, y좌표, x좌표 넣기
    visited[0][0] = rupee[0][0]   # 시작지점 루피

    while queue:
        d, y, x = heapq.heappop(queue)  # 현재까지 잃은 루피, 현재 좌표 꺼내기

        if y == n-1 and x == n-1:   # 동굴 출구까지 왔다면 현재까지 잃은 루피 출력
            print(f'Problem {tc}: {d}')
            return

        if visited[y][x] < d:   # 현재까지 잃은 루피가 저장되어 있는 루피보다 크다면 패스
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n: # 다음 갈 곳이 범위 내에 있다면
                nd = d + rupee[ny][nx]  # 현재까지 잃은 루피 + 다음 위치에서 잃을 루피
                if nd < visited[ny][nx]:    # 그 루피가 저장되어 있는 루피보다 적다면 갱신
                    visited[ny][nx] = nd
                    heapq.heappush(queue, [nd, ny, nx]) # 가보기

tc = 1
while True:
    n = int(input())    # 동굴의 크기
    if n == 0:  # 0 입력이 주어지면 전체 입력 종료
        break
    rupee = [list(map(int, input().split())) for _ in range(n)] # 도둑루피

    visited = [[float('inf') for _ in range(n)] for _ in range(n)]
    dijkstra()

    tc += 1


def dfs(y, x, k):
    global answer
    global end

    if end and answer < k:
        return

    if y == n-1 and x == n-1:
        end = True
        if k < answer:
            answer = k
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, k + rupee[ny][nx])
            visited[ny][nx] = False

# tc = 1
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     rupee = [list(map(int, input().split())) for _ in range(n)]
#
#     visited = [[False for _ in range(n)] for _ in range(n)]
#     answer = 99999999999
#     end = False
#     dfs(0, 0, rupee[0][0])
#     print(f'Problem {tc}: {answer}')
#
#     tc += 1



