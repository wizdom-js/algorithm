import heapq


def dijkstra(n, s, summits, point_info):
    dist = [float('inf') for _ in range(n + 1)]
    queue = []
    heapq.heappush(queue, [0, s])
    dist[s] = 0
    while queue:
        d, now = heapq.heappop(queue)

        if now in summits:
            return d

        for nxt in point_info[now]:
            nd = nxt[1] + d

            if nd < dist[nxt[0]]:
                dist[nxt[0]] = nd
                heapq.heappush(queue, [nd, nxt[0]])


from collections import deque


def solution(n, paths, gates, summits):
    point_info = [[] for _ in range(n + 1)]
    for point1, point2, time in paths:
        point_info[point1].append([point2, time])

    max_time = 99999999
    candi = []

    def bfs(s):
        queue = deque([[s, 0]])
        while queue:
            now, tmp_t = queue.popleft()
            for nxt, time in point_info[now]:
                if nxt not in summits:
                    queue.append([nxt, max(tmp_t, time)])
                else:
                    candi.append([nxt, tmp_t])

    for gate in gates:
        tmp = bfs(gate)

    candi.sort(key=lambda x: [x[1], x[0]])
    print(candi)




