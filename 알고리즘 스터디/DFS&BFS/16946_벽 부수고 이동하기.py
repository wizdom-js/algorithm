import sys
sys.stdin = open('input.txt')

from collections import deque
'''
1을 만날 때 bfs 탐색하면 중복 탐색이 많으므로 시간 초과
그렇다면 반대로 해보면 어떨까 하고 나오게 된 풀이
1. for문을 돌면서 0을 만날 때 bfs 탐색을 해서 이어져있는 칸의 개수를 세어준다. 
2. 다시 for문을 돌면서 1을 만날 때 1에서의 상하좌우에서 이어져 있는 칸의 개수를 자기 자리에 더해준다.
3. 상하좌우에서 중복된 구역이 있을 수 있으므로 제거해준다.
'''
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(y, x, section_idx):
    queue = deque([[y, x]])
    visited[y][x] = 1   # 시작 지점 방문 처리 
    cnt = 1 # 시작 지점부터 count
    while queue:
        y, x = queue.popleft()
        sections[y][x] = section_idx    # 해당 자리에 구역 번호 넣어주기 
        for i in range(4):
           ny, nx = dy[i] + y, dx[i] + x
           if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx]:  # 범위 벗어나지 않고 방문하지 않은 곳이라면 
               if not map_info[ny][nx]:     # 이동할 수 있는 곳이라면 (0이라면)
                   queue.append([ny, nx])   # 해당 자리 가보기 
                   visited[ny][nx] = 1 
                   cnt += 1
    return cnt # 이어진 칸 수 반환 

m, n = map(int, sys.stdin.readline().rsplit())  # 세로, 가로 
map_info = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(m)]    # 맵 
sections = [[0 for _ in range(n)] for _ in range(m)]    # 구역 인덱스 정보 
visited = [[0 for _ in range(n)] for _ in range(m)]     # 방문 처리 리스트 

# 이동할 수 있는 곳의 구역 조사  
section_sizes = [0] # 구역 사이즈가 들어갈 리스트 
section_idx = 1     # 구역 인덱스 초기화
for i in range(m):
    for j in range(n):
        if not map_info[i][j] and not visited[i][j]:    # 이동할 수 있는 곳이고 방문하지 않은 곳이라면 
            section_sizes.append(bfs(i, j, section_idx))    # bfs 탐색으로 이어진 구역의 개수를 세어서 해당 인덱스에 저장한다. 
            section_idx += 1    # 구역 번호 + 1

# 벽에서 상하좌우 탐색하여 더하기 => 이동할 수 있는 칸의 개수 
for y in range(m):
    for x in range(n):
        if map_info[y][x]:  # 벽이라면 
            connected_s = set() # 구역 중복 방지를 위한 set 
            for i in range(4):  # 상하좌우 탐색 
                ny, nx = dy[i] + y, dx[i] + x
                if 0 <= ny < m and 0 <= nx < n:
                    connected_s.add(sections[ny][nx])   # 해당 구역의 인덱스 추가 
            for i in connected_s:   # 맞닿아 있는 구역의 크기 더하기 => 크기만큼 이동할 수 있는 것이므로 
                map_info[y][x] += section_sizes[i]
                map_info[y][x] %= 10    # 이동할 수 있는 칸의 개수를 10으로 나눈 나머지로 변환 

for i in range(m):
    for j in range(n):
        print(map_info[i][j], end='')
    print()


# bfs로 풀었던 처음 풀이 (1 만나면 갈 수 있는 구역 bfs로 탐색) 
'''
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(y, x):
    visited = [[0 for _ in range(n)] for _ in range(m)]
    queue = deque([[y, x]])
    visited[y][x] = 1
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
           ny, nx = dy[i] + y, dx[i] + x
           if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx]:
               if not map_info[ny][nx]:
                   queue.append([ny, nx])
                   visited[ny][nx] = 1
                   cnt += 1
    return cnt 

m, n = map(int, sys.stdin.readline().rsplit())
print(n, m)
map_info = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(m)]
answer = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        if map_info[i][j]:
            map_info[i][j] == 0
            cnt = bfs(i, j)
            map_info[i][j] == 1
            answer[i][j] = cnt % 10

for i in range(m):
    for j in range(n):
        print(answer[i][j], end='')
    print()
'''
