import sys
sys.stdin = open('input.txt')

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]
for i in range(n-1, -1, -1):
    day = schedule[i][0]
    price = schedule[i][1]
    if i + day <= n:
        dp[i] = max(dp[i+1], dp[i + day] + price)
    else:
        dp[i] = dp[i+1]


    print(day, price)
    print(i, dp)

print(dp[0])