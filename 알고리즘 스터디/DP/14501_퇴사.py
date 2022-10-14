import sys
sys.stdin = open('input.txt')

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]
# 탑 다운 방식
for i in range(n-1, -1, -1):
    day = schedule[i][0]
    price = schedule[i][1]
    if i + day <= n:    # 상담 일이 기간 내라면
        dp[i] = max(dp[i+1], dp[i + day] + price)   # 지금 상담 선택 안하기 vs 지금 상담 비용 + 지금 상담 후 날짜의 비용
    else:               # 기간 넘는 경우
        dp[i] = dp[i+1]

print(dp[0])