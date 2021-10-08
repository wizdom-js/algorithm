import sys
sys.stdin = open('input.txt')

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]    # S마켓에서 사용하는 돈의 종류

tc = int(input())
for idx in range(1, tc+1):
    target = int(input())   # 손님에게 거슬러 주어야 할 금액
    used = [0 for _ in range(8)]    # 돈 종류 별로 몇개씩 필요한지 저장할 배열

    for i in range(8):
        if money[i] <= target:  # 돈이 목표 돈보다 작은경우 (큰 경우는 거슬러 줄 수 없음)
            used[i] = target//money[i]  # 사용할 개수만큼 used의 해당 인덱스에 저장
            target %= money[i]      # money[i]를 사용하고 남은 돈

        if not target:  # 거슬러 주어야할 금액 이제 없다면 끝
            break

    print('#{}'.format(idx))
    print(*used)


