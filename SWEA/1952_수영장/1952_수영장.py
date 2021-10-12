import sys
sys.stdin = open('sample_input.txt')


tc = int(input())
for idx in range(1, tc+1):
    charge = list(map(int, input().split()))    # 1일, 1달, 3달, 1년
    plan = list(map(int, input().split()))  # 1월부터 12월까지의 이용 계획

    dp = [0 for _ in range(12)]
    for i in range(12):
        dp[i] = dp[i-1] + min(plan[i] * charge[0], charge[1]) # 이전 달의 요금 + (1일 이용권으로 계산 vs 1달 이용권으로 계산)
        if i > 1:   # 3달 이상 됐다면
            dp[i] = min(dp[i], dp[i-3] + charge[2])   # 3달 이용권으로 할까 말까

    print('#{} {}'.format(idx, min(dp[-1], charge[3]))) # 1년 이용권으로 할까 말까