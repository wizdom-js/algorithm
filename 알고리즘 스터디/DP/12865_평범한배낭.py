import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())    # 물품의 수 n, 버틸 수 있는 무게 k
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]    # [물건의 무게, 물건의 가치]

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    w = arr[i][0]
    v = arr[i][1]
    for j in range(1, k+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[n][k])

