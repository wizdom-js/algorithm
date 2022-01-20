import heapq


# 지점의 개수, 출발지점, a의 도착지점, b의 도착지점, 지점 사이의 예상 택시요금
def solution(n, s, a, b, fares):
    visit = [[] for _ in range(n + 1)]
    for p1, p2, fare in fares:
        visit[p1].append([p2, fare])
        visit[p2].append([p1, fare])

    def dijkstra(s, e):
        dist = [1e9 for _ in range(n + 1)]
        queue = [[0, s]]
        dist[s] = 0
        while queue:
            d, now = heapq.heappop(queue)

            if now == e:
                return d

            if dist[now] < d:
                continue

            for next in visit[now]:
                nd = d + next[1]

                if nd < dist[next[0]]:
                    dist[next[0]] = nd
                    heapq.heappush(queue, [nd, next[0]])
        return 0

    answer = 1e9
    for i in range(1, n + 1):
        tmp = dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b)
        if tmp and tmp < answer:
            answer = tmp

    return answer