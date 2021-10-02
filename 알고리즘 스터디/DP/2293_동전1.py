import sys
sys.stdin = open('input.txt')


n, k = map(int, input().split())    # 동전 종류 수 n, 목표 가치 k
coins = [int(input()) for _ in range(n)]    # 동전들

dp = [0 for _ in range(100001)] # dp 배열

for c in coins:
    dp[c] += 1
    for i in range(k-c+1):
        dp[i+c] += dp[i]

print(dp[k])

