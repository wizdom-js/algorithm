import sys
sys.stdin = open('sample_input.txt')

import heapq

tc = int(input())
for idx in range(1, tc+1):
    n, e = map(int, input().split())
    temp = [list(map(int, input().split())) for i in range(e)]

    dist = [999999999 for i in range(n+1)]
    visited = [[] for i in range(n+1)]
    for i in temp:
        visited[i[0]].append([i[1], i[2]])

    que = []
    heapq.heappush(que, [0, 0])
    dist[0] = 0

    while que:
        d, now = heapq.heappop(que)
        if now == n:
            print('#{} {}'.format(idx, d))
            break

        if d > dist[now]:
            continue

        for i in visited[now]:
            nd = dist[now] + i[1]
            if dist[i[0]] > nd:
                dist[i[0]] = nd
                heapq.heappush(que, [nd, i[0]])