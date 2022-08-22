import heapq


def solution(n, paths, gates, summits):
    def find_intensity():
        dist = [float('inf') for _ in range(n + 1)]

        queue = []
        for gate in gates:
            heapq.heappush(queue, [0, gate])
            dist[gate] = 0

        while queue:
            intensity, now = heapq.heappop(queue)

            if now in summits:
                continue

            if dist[now] < intensity:
                continue

            for nxt, nxt_i in point_info[now]:
                choosed_i = nxt_i if nxt_i > intensity else intensity
                if choosed_i < dist[nxt]:
                    dist[nxt] = choosed_i
                    heapq.heappush(queue, [choosed_i, nxt])

        answer = [0, 9999999999]
        for summit in summits:
            if dist[summit] < answer[1]:
                answer[0] = summit
                answer[1] = dist[summit]

        return answer

    point_info = [[] for _ in range(n + 1)]

    for point1, point2, time in paths:
        point_info[point1].append([point2, time])
        point_info[point2].append([point1, time])

    return find_intensity()




