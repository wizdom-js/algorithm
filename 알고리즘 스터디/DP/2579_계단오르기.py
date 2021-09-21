import sys
sys.stdin = open('input.txt')


n = int(input()) # 계단의 수
stairs = [int(input()) for _ in range(n)] # 계단

if n == 1:
    print(stairs[0])

else:
    dp = [0 for _ in range(n)]

    dp[0] = stairs[0]   # 1번 계단
    dp[1] = stairs[0] + stairs[1] # 1번 + 2번 계단 밟음
    for i in range(2, n):
        # 1. 현재 계단 + 이전의 계단 + 전전전의 계단 밟은 경우
        # 2. 현재 계단 + 전전의 계단 밟은 경우
        # 두 경우 중 더 큰 값을 선택
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

    print(dp[n-1])