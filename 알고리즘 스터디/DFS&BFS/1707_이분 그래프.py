import sys
sys.stdin = open('input.txt')

# 이분그래프 : 인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프
# 그래프의 모든 정점이 두 그룹으로 나눠지고 서로 다른 그룹의 정점이 간선으로 연결되어져있는 (같은 그룹에 속한 정점끼리는 서로 인접하지 않도록 하는) 그래프

from collections import deque


# DFS를 활용하여 이분그래프 판별 (재귀에러)
def dfs(now, color):
    global is_bipartite
    node_color[now] = color # 하나의 색으로 칠하기
    for next in graph[now]: # 인접한 곳 탐색
        if not node_color[next]:    # 색이 칠하지 않은 곳이면 반대 색을 가지고 들어가기
            dfs(next, -color)
        elif node_color[next] == node_color[now]:   # 현재 정점의 색과 다음 갈 곳의 색이 같다면 => 이분그래프가 아님
            is_bipartite = False
            return


# BFS를 활용하여 이분그래프 판별하기
def bfs(s):
    queue = deque([s])
    node_color[s] = 1   # 출발 정점 1로 칠하기
    while queue:
        now = queue.popleft()
        for next in graph[now]: # 인접한 곳 탐색
            if not node_color[next]:    # 다음 정점이 아직 색칠하지 않은 곳이면
                node_color[next] = -node_color[now] # 반대 색으로 색칠하고 다음 정점로 이동
                queue.append(next)
            elif node_color[next] == node_color[now]:   # 현재 정점 색과 다음 정점 색이 같으면 => 이분그래프 아님
                return False
    return True


k = int(input())    # 테스트 케이스의 수

for _ in range(k):
    v, e = map(int, input().split())    # 그래프 정점의 개수 v, 간선의 개수 e
    graph = [[] for _ in range(v + 1)]  # 인접 리스트 만들기
    for _ in range(e):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    is_bipartite = True

    node_color = [0 for _ in range(v + 1)]  # 정점들의 색을 표시할 배열
    for i in range(1, v + 1):
        if not node_color[i]:   # 아직 색 칠하지 않은 노드라면
            # dfs(i, 1)
            if not bfs(i):  # 색 칠했는데 이분그래프 아니라고 나온다면 ? (False 반환했다면)
                is_bipartite = False    # 이분그래프 아니라고 변경하고 반복문 중단
                break
        # if not is_bipartite:
        #     break

    print('YES' if is_bipartite else 'NO')