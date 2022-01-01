import sys
sys.stdin = open('input.txt')

n = int(input())    # 도시의 수 n
cost = [list(map(int, input().split())) for _ in range(n)]  # 비용 행렬
dp = [[1e9 for _ in range(1 << n)] for _ in range(n)]

def recur(city, visit):
    if visit == (1 << n) - 1:   # 모든 도시 방문했다면
        if cost[city][0]:       # 출발점으로 가는 경로가 있다면 (출발하는 도시 0으로 정했으므로)
            return cost[city][0]    # 비용 리턴
        return 1e9  # 출발점으로 가는 경로 없는 경우

    if dp[city][visit] != 1e9:  # 최소비용 메모이제이션 해놓았다면 꺼내쓰기
        return dp[city][visit]

    for i in range(1, n):   # 모든 도시 탐방 (출발 도시 제외)
        if not cost[city][i]:   # 가는 경로가 없다면 skip
            continue

        if visit & (1 << i):    # 이미 방문한 도시라면 skip
            continue

        # 점화식
        # 현재 비용 + 방문안한 도시 다 탐방한 비용 vs 저장되어 있는 비용
        dp[city][visit] = min(recur(i, visit | (1 << i)) + cost[city][i], dp[city][visit])

    return dp[city][visit]

print(recur(0, 1))  # 순서 상관 x 사이클의 최소비용을 구하면 되니까 임의의 도시 0에서 시작 (0번째 도시, 방문했다 1)
for i in range(n):
    print(dp[i])