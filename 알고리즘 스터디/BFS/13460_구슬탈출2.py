import sys
sys.stdin = open('input.txt')

# 좌, 우, 상, 하
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def start_point(y, x, string):
    if not y and string in line:
        y = i
        x = line.index(string)
    return y, x


def BFS(G, v, n):							# 그래프 G, 탐색 시작점 v
  	visited = [0] * (n+1)			# n: 정점의 개수 (1번부터 시작하니까 인덱스 맞춰주려고 n+1)
    queue = []								# 큐 생성
    queue.append(v)						# 시작점 v를 큐에 삽입 (enQueue)
    while queue:							# 큐가 비어있지 않은 경우
      	t = queue.pop(0)			# 큐의 첫번째 원소 반환
        if not visitied[t]:			# 방문되지 않은 곳이라면
          	visited[t] = True		# 방문한 것으로 표시
            visit(t)						# 정점 t에서 할 일
        		for i in G[t]:					# t와 연결된 모든 정점에 대해
                if not visited[i]:	# 방문되지 않은 곳이라면
                    queue.append(i)	# 큐에 넣기

def tilt(y, x, v_list, cnt):
    queue = [(y, x)]
    while queue:
        ty, tx = queue.pop(0)
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if board[ny]

        if board[ny][nx] == '.' and not v_list[y][x]:
            go_or_not = straight(y, x, v_list)
            if go_or_not:
                tilt(go_or_not[0], go_or_not[1], v_list)



def straight(y, x, v_list):
    visited = []
    while True:
        y += dy[i]
        x += dx[i]

        if board[y][x] == '.':
            visited.append((y, x))
            continue
        else:
            for j in range(4):
                if j != i :
                    ny = y + dy[j]
                    nx = x + dx[j]
                    if board[ny][nx] == '.':
                        for v in visited:
                            v_list[v[0]][v[1]] = 1
                        return ny, nx
            return False








n, m = map(int, input().split())
ry = rx = False
by = bx = False
oy = ox = False
a_visited = [[0 for _ in range(n)] for _ in range(n)]
b_visited = [[0 for _ in range(n)] for _ in range(n)]
board = []
for i in range(n):
    line = list(input())
    ry, rx = start_point(ry, rx, 'R')
    by, bx = start_point(by, bx, 'B')
    oy, ox = start_point(oy, ox, 'O')

