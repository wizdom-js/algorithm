import sys
sys.stdin = open('input.txt')

import heapq

# find(root 찾기) 
def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

# union(x, y 연결)
def union(x, y):
    x = find(x)
    y = find(y)
    root[x] = y

city_n, road_n, cost = map(int, input().split()) # 도시의 개수, 도로의 개수, 한번 정복할 때마다 증가하는 도로의 비용
root = list(range(city_n + 1))  # 루트 배열  

tmp = []
for _ in range(road_n):
    road_a, road_b, road_cost = map(int, input().split())   # 도로 a, 도로 b, a b 사이 도로의 비용
    heapq.heappush(tmp, (road_cost, road_a, road_b))        # 비용이 작은 것부터 꺼내서 정복할 것이므로 heapq 사용
    
answer = 0
i = 0   # 정복한 도시 개수 
for _ in range(road_n):
    road_cost, road_a, road_b = heapq.heappop(tmp)  # 비용이 작은 것부터 꺼내기 
    if find(road_a) != find(road_b):    # 부모가 같지 않다면 
        union(road_a, road_b)   # 정복 
        answer += road_cost + (i*cost)  # 비용 더하기 
        i += 1  # 도시 한번 정복할 때마다 도로의 비용이 증가하니 +1

print(answer)