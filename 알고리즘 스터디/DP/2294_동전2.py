import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 최소 개수 출력이므로 최댓 값으로 채우기
dp = [100001 for _ in range(k+1)]
dp[0] = 0
for c in coins:
    # 해당 동전(c)를 사용하여 i원에 필요한 동전 개수 넣어주기
    for i in range(c, k+1):
        # 점화식 =>
        # 현재 동전 사용하여 i원 만들기 (그러려면 i원 - c원에서 사용된 최소 동전 개수 + 현재 동전 (c))
        # vs
        # 다른 동전들을 사용하여 i원 만들기(현재 동전 사용 x)
        dp[i] = min(dp[i-c] + 1, dp[i])

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])
