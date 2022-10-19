import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra(store):
    dist = [float('inf') for _ in range(v_n + 1)]
    min_distance = 0
    queue = []
    if store == "m":
        min_distance = mac_distance
        for mac in mac_v:
            heapq.heappush(queue, [0, mac])
    else:
        min_distance = star_distance
        for star in star_v:
            heapq.heappush(queue, [0, star])

    while queue:
        d, now = heapq.heappop(queue)

        if dist[now] < d:
            continue

        for nxt in visit[now]:
            nd = nxt[1] + d

            if nd < dist[nxt[0]] and nd <= min_distance:
                dist[nxt[0]] = nd
                heapq.heappush(queue, [nd, nxt[0]])

    return dist


input_form = sys.stdin.readline().split()
v_n, road_n = map(int, input_form)    # 정점의 개수, 도로의 개수

visit = [[] for _ in range(v_n + 1)]
for _ in range(road_n):
    road1, road2, w = map(int, input_form)
    visit[road1].append([road2, w])
    visit[road2].append([road1, w])

mac_n, mac_distance = map(int, input_form)
mac_v = list(map(int, input_form))

star_n, star_distance = map(int, input_form)
star_v = list(map(int, input_form))

mac_dist = dijkstra("m")
star_dist = dijkstra("s")

answer = float('inf')
for i in range(1, v_n + 1):
    distance = mac_dist[i] + star_dist[i]
    if distance < answer:
        answer = distance

if answer == float('inf'):
    answer = -1

print(answer)
