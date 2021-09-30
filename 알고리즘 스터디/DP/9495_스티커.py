import sys
sys.stdin = open('input.txt')
#
# tc = int(input())
#
# for _ in range(tc):
#     n = int(input())    # 한 라인의 스티커 개수
#     sticker = [list(map(int, input().split())) for _ in range(2)]   # 주어진 스티커 배열
#
#     dp = [[0 for _ in range(n)] for _ in range(2)]  # dp 배열
#     dp[0][0] = sticker[0][0] # 초기 스티커 넣어주기
#     dp[1][0] = sticker[1][0]
#     if n == 1:
#         print(max(dp[0][0], dp[1][0]))
#     else:
#         dp[0][1] = sticker[1][0] + sticker[0][1]
#         dp[1][1] = sticker[0][0] + sticker[1][1]
#         for i in range(2, n):
#             dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + sticker[0][i] # 더 큰 dp찾아서 현재 스티커와 더해주기
#             dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + sticker[1][i]
#
#         print(max(dp[0][-1], dp[1][-1]))    # 마지막 자리에서 여태까지 더한 제일 큰 점수 선택

####################################3

tc = int(input())

for _ in range(tc):
    n = int(input())    # 한 라인의 스티커 개수
    dp = [list(map(int, input().split())) for _ in range(2)]   # 주어진 스티커 배열

    if n > 1:
        dp[0][1] += dp[1][0]    # 점화식에 i-2가 있기때문에 처음 값은 직접 더해준다. (현재자리의 왼쪽 대각선자리)
        dp[1][1] += dp[0][0]
        for i in range(2, n):
            dp[0][i] += max(dp[1][i-2], dp[1][i-1]) # 더 큰 dp찾아서 현재 스티커와 더해주기
            dp[1][i] += max(dp[0][i-2], dp[0][i-1])

    print(max(dp[0][-1], dp[1][-1]))    # 마지막 자리에서 여태까지 더한 제일 큰 점수 선택

'''
6
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
5
9 1 1 1 9
1 1 9 1 1
4
100 1 1 100
1 1 100 1
5
1 0 1 0 9
0 1 9 9 9
3
1 999 0
1 0 999
2
1 2
3 1
6
20 5 30 9 19 0
30 9 10 0 30 14
4
50 40 19 18
40 20 40 20
4
40 40 39 40
40 40 40 40
4
10 5 10 5
30 10 5 30
1
1
2

260 290 27 300 21 1999 5 93 138 160 70 2
'''