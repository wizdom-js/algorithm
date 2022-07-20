import sys
sys.stdin = open('input.txt')

from collections import deque


def is_loop(now, move):
    visited[now] = True

    for next in station_info[now]:
        if not visited[next]:
            is_loop(next, move+1)
        elif next == start and move > 1:
            loop_station[start] = True
            return


def get_distance(s):
    queue = deque([[s, 0]])
    visited = [0 for _ in range(n)]
    while queue:
        now, move = queue.popleft()
        visited[now] = True

        for next in station_info[now]:
            if loop_station[next]:
                print(move + 1, end=' ')
                return
            elif not visited[next]:
                queue.append([next, move+1])


n = int(input()) + 1
station_info = [[] for _ in range(n)]
graph_size = [0 for _ in range(n)]
for _ in range(n-1):
    station1, station2 = map(int, input().split())
    station_info[station1].append(station2)
    station_info[station2].append(station1)
    graph_size[station1] += 1
    graph_size[station2] += 1

loop_station = [True for _ in range(n)]
loop_station[0] = False
# for start in range(1, n):
#     visited = [0 for _ in range(n)]
#     is_loop(start, 0)
while 1 in graph_size:
    for i in range(1, n):
        if graph_size[i] == 1:
            graph_size[i] = 0
            loop_station[i] = False
            graph_size[station_info[i][0]] -= 1
            station_info[station_info[i][0]].remove(i)

for station in range(1, n):
    if loop_station[station]:
        print(0, end=' ')
    else:
        get_distance(station)