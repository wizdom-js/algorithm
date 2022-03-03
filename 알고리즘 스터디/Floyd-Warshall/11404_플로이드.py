import sys
sys.stdin = open('input.txt')

city_n = int(input())
bus_n = int(input())

dist = [[1e9 for _ in range(city_n)] for _ in range(city_n)]

# 버스 정보 받아와서 넣어주기 
for _ in range(bus_n):
    s, e, c = map(int, input().split()) # 버스 시작 도시 s, 도착 도시 e, 필요한 비용 c
    dist[s-1][e-1] = min(dist[s-1][e-1], c) # 시작과 도착을 연결하는 노선은 하나 이상일 수 있음

# 플로이드 워셜 
for k in range(city_n): # 경유지 
    dist[k][k] = 0 # 자기 자신 비용은 0
    for i in range(city_n): # 출발
        for j in range(city_n): # 도착 
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])   # 저장되어있는 비용 vs 경유지를 거치는 비용 

for i in range(city_n):
    for j in range(city_n):
        if dist[i][j] == 1e9:   # i에서 j로 갈 수 없는 경우 
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
