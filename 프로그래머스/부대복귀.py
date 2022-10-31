from collections import deque

from collections import deque


# 더 빠른 풀이
def solution(n, roads, sources, destination):
    area_info = [[] for _ in range(n + 1)]
    for area1, area2 in roads:
        area_info[area1].append(area2)
        area_info[area2].append(area1)

    distance = [-1 for _ in range(n + 1)]
    distance[destination] = 0
    queue = deque([destination])

    while queue:
        now = queue.popleft()

        for nxt in area_info[now]:
            if distance[nxt] == -1:
                distance[nxt] = distance[now] + 1
                queue.append(nxt)

    answer = [distance[s] for s in sources]
    return answer

# 처음 풀이
def solution(n, roads, sources, destination):
    def bfs(s):
        queue = deque([[s, 0, [0]]])
        visited = [0 for _ in range(n + 1)]
        visited[s] = True
        while queue:
            now, move, visit = queue.popleft()
            if now == destination:
                return [move, visit]

            for nxt in area_info[now]:
                if not visited[nxt]:
                    visited[nxt] = True
                    visit.append(nxt)
                    queue.append([nxt, move + 1, visit])

        return -1, []

    area_info = [[] for _ in range(n + 1)]
    for area1, area2 in roads:
        area_info[area1].append(area2)
        area_info[area2].append(area1)

    answer = []
    distance = [0 for _ in range(n + 1)]
    for s in sources:
        if distance[s]:
            answer.append(distance[s])
        else:
            result = bfs(s)
            move, visit = result[0], result[1]
            answer.append(move)
            distance[s] = move
            for v in visit[:-1:-1]:
                move -= 1
                distance[v] = move

    return answer