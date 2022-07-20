import sys
sys.stdin = open('input.txt')

from collections import deque

def dfs(now, color):
    global is_bipartite
    node_color[now] = color
    for next in graph[now]:
        if not node_color[next]:
            dfs(next, -color)
        elif node_color[next] == node_color[now]:
            is_bipartite = False
            return

def bfs(s):
    queue = deque([s])

    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if not node_color[next]:
                node_color[next] = -node_color[now]
                queue.append(next)
            elif node_color[next] == node_color[now]:
                return False
    return True

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())    # 그래프 정점의 개수 v, 간선의 개수 e
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    is_bipartite = True

    node_color = [0 for _ in range(v + 1)]
    for i in range(1, v + 1):
        if node_color[i] == 0:
            # dfs(i, 1)
            node_color[i] = 1
            if not bfs(i):
                is_bipartite = False
                break
        # if not is_bipartite:
        #     break

    print('YES' if is_bipartite else 'NO')