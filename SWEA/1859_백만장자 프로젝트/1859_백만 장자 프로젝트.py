import sys
sys.stdin = open('input.txt')

######### 구현 ############

# 매도
def sell(benefit, today, buy):
    # 산거 다 팔때까지 반복
    while buy:
        # 오늘 포인트에서 샀던거 차이 만큼 더해주기
        benefit += (today - buy.pop())
    return benefit


t = int(input())

for idx in range(1, t+1):
    n = int(input())
    # pop 사용할거기 때문에 받아온 매매가들을 뒤집어 준다.
    deal = list(map(int, input().split()))[::-1]

    buy = []        # 매수한 리스트
    benefit = 0     # 이익

    max_point = max(deal)   # 최고 주가

    while deal:
        today = deal.pop()  # 오늘 주가

        # 오늘 매매가가 최고 주가 보다 작다면 매수
        if today < max_point:
            buy.append(today)

        # 오늘 매매가가 최고 주가라면
        else:
            benefit = sell(benefit, today, buy) # 매도
            if deal:  # 다시 최고 주가 구하기
                max_point = max(deal)

    print('#{} {}'.format(idx, benefit))
