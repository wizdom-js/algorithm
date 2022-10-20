import sys
sys.stdin = open('input.txt')

testcase = int(input())
for _ in range(testcase):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    # 처음 스티커 두 장 넣기
    dp[0][1] = stickers[0][0]
    dp[1][1] = stickers[1][0]
    for i in range(2, n+1):
        # 점화식
        # 대각선의 점수를 택할 것인지 vs 대각선 바로 옆에 있는 점수를 택할 것인지
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[0][i-1]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i-1]

    # 첫 번째 스티커에서 출발한 점수 vs 두 번째 스티커에서 출발한 점수
    print(max(dp[0][-1], dp[1][-1]))