import sys
sys.stdin = open('input.txt')

################ 그리디 ################
# 거꾸로 간다. 과거로 이동하면서 현재보다 더 높은 지점이 있다면 저장했다가 최고 높은 지점과 이동한 지점의 차익을 더한다.

t = int(input())

for idx in range(1, t+1):
    n = int(input())
    deal = list(map(int, input().split()))

    benefit = 0     # 이익
    max_point = deal.pop()  # 최고 주가

    while deal:
        today = deal.pop()  # 오늘 주가

        # 오늘 주가가 미래의 최고 주가 보다 작다면 차익 더하기
        if today < max_point:
            benefit += (max_point - today)

        # 오늘 주가가 최고 주가보다 크면 바꿔주기
        else:
            max_point = today


    print('#{} {}'.format(idx, benefit))
