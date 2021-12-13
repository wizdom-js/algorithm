import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())    # 물품의 수 n, 버틸 수 있는 무게 k
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]    # [물건의 무게, 물건의 가치]

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    w = arr[i][0]   # 현재 물건의 무게
    v = arr[i][1]   # 현재 물건의 가치
    for j in range(1, k+1):
        if j < w:   # 무게 j보다 현재 물건의 무게가 더 무겁다면
            dp[i][j] = dp[i-1][j]   # 바로 이전 물건, 같은 무게로 채우기
        else:       # 무게 j보다 현재 물건의 무게가 같거나 더 가볍다면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
            # 이전 물건에서의 j무게 일때의 가치 vs 현재 물건의 가치 + 남은 무게를 다른 물건으로 채운 가치
            # 둘 중 더 가치있는 것을 선택

print(dp[n][k]) # 물품 모두 검토해보고, 버틸 수 있는 무게 k일때 가장 최대 가치
# print(dp[-1][-1])

