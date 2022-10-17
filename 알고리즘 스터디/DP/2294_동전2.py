import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [999999999 for _ in range(100001)]
dp[0] = 0
for c in coins:
    dp[c] = 1
    for i in range(c, k+1):
        dp[i] = min(dp[i-c] + 1, dp[i])

if dp[k] == 999999999:
    print(-1)
else:
    print(dp[k])
