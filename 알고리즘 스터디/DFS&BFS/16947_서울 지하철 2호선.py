import sys
sys.stdin = open('input.txt')

from collections import deque


# dfs를 활용한 루프 찾기
def is_loop(now, move):
    visited[now] = True # 방문처리

    for next in station_info[now]:  # 현재 역이랑 이어진 역 가기
        if not visited[next]:
            is_loop(next, move+1)   # 방문하지 않은 역이면 들어가기
        elif next == start and move > 1:    # 다음 역이 처음 시작한 역이었고 다른 역을 거쳐서 온 것이라면 ?(순환역이라면)
            loop_station[start] = True  # 해당 역 순환역이라고 표시
            return


# bfs를 활용하여 순환역까지의 거리 찾기
def get_distance(s):
    queue = deque([[s, 0]]) # 처음 시작 역과 이동한 거리(0) 넣기
    visited = [0 for _ in range(n)] # 방문처리 배열
    while queue:
        now, move = queue.popleft()
        visited[now] = True # 방문 처리 하기

        for next in station_info[now]:  # 현재 역에서 이어진 역 가보기
            if loop_station[next]:  # 다음 역이 순환역이면 바로 거리 출력
                print(move + 1, end=' ')
                return
            elif not visited[next]: # 다음 역이 순환역이 아니고 방문하지 않은 곳이면 방문하기
                queue.append([next, move+1])


n = int(input()) + 1    # 역의 수
station_info = [[] for _ in range(n)]   # 인접 리스트
graph_size = [0 for _ in range(n)]  # 역마다의 간선 수 기록
for _ in range(n-1):
    station1, station2 = map(int, input().split())
    station_info[station1].append(station2)
    station_info[station2].append(station1)
    graph_size[station1] += 1
    graph_size[station2] += 1

loop_station = [True for _ in range(n)] # 해당 역이 순환역인지의 여부
loop_station[0] = False

# dfs 활용하여 순환역 찾기
# for start in range(1, n):
#     visited = [0 for _ in range(n)]
#     is_loop(start, 0)

# 순환역이 아닌 역들 끝에서부터 지워나가며 순환역만 남기기
while 1 in graph_size:  # 이어진 역이 1개인 역이 없을 때까지 반복 (순환역은 최소 2개)
    for i in range(1, n):
        if graph_size[i] == 1:  # 이어진 역이 하나 뿐이라면 => 순환역 아니라면
            graph_size[i] = 0   # 간선 수 0으로 만들기
            loop_station[i] = False # 해당 역 순환역이 아니라고 표시
            graph_size[station_info[i][0]] -= 1 # 이어진 역도 간선 하나 빼주고 해당 역 인접리스트에서 지우기
            station_info[station_info[i][0]].remove(i)

for station in range(1, n):
    if loop_station[station]:   # 순환역이면 0 출력
        print(0, end=' ')
    else:
        get_distance(station)   # 순환역이 아니라면 거리 찾기 