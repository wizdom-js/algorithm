import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra(s):
    dist = [float('inf') for _ in range(n+1)]
    queue = []
    heapq.heappush(queue, [0, s])
    dist[s] = 0
    while queue:
        d, now = heapq.heappop(queue)

        if dist[now] < d:
            continue

        for nxt, nxt_d in network[now]:
            new_d = nxt_d + d
            if new_d < dist[nxt]:
                # 모든 컴퓨터에서 최단 거리를 찾아야 한다.
                # 해당 컴퓨터에서 더 짧은 거리가 있으면 connecting_info(이어질 컴퓨터) 갱신
                connecting_info[nxt] = now
                dist[nxt] = new_d
                heapq.heappush(queue, [new_d, nxt])


n, m = map(int, input().split())

network = [[] for _ in range(n+1)]
for _ in range(m):
    com1, com2, time = map(int, input().split())
    network[com1].append([com2, time])
    network[com2].append([com1, time])

connecting_info = [0 for _ in range(n+1)]
dijkstra(1)

print(n-1)  # 모든 컴퓨터가 이어지는 것이니 n-1
for i in range(2, n+1):
    print(i, connecting_info[i])


# 처음 시도한 방법 => 모든 컴퓨터에서 시작해서 해당 컴퓨터에서 가장 짧은 곳을 골라서 출력하는 방식
# 지금 와서 생각해보면 다익스트라 함수의 시작 노드에서 젤 처음으로 골라진 노드를 출력하면 될 일이었다.
# connected_list = set()
# connecting_cnt = 0
# answer = []
# for i in range(1, n+1):
#     connected_info = dijkstra(i)
#
#     tmp_node = 0
#     tmp_time = 9999999
#     for j in range(1, n+1):
#         if i == j: continue
#         if connected_info[j] < tmp_time:
#             tmp_node = j
#             tmp_time = connected_info[j]
#
#     connected_list.add((i, tmp_node))
#     connected_list.add((tmp_node, i))
#
#     if len(connected_list) == connecting_cnt: continue
#
#     answer.append([i, tmp_node])
#     connecting_cnt += 2
#
# print(connecting_cnt//2)
# for com1, com2 in answer:
#     print(com1, com2)
