import sys
sys.stdin = open('input.txt')

# * 자신의 차례에 가져올 돌이 없으면 지는 게임 *
t = int(input())
for _ in range(t):
    n = int(input())    # 돌 개수

    # 순서 : 승우(0) -> 상윤(1)
    if n % 10:
        print(0)
    else:
        print(1)

    # 10의 배수인 경우는 승우가 아무리 머리를 쓰더라도 상윤이가 이기게 된다.
    # 예) n = 10 / 승: 9 / 상: 1 => 승우가 가져올 돌이 없으므로 상윤 승
    # 예) n = 20 / 승: 8 / 상: 1 => n = 10이 되므로 상윤 승
    # 예) n = 50 / 승: 22 / 상: 8 => n = 20이 되므로 상윤 승

    # 10의 배수가 아닌 경우에는 승우가 무조건 이기게 된다.
    # 예) n이 한자리 수인 경우, 승우가 다 가져가면 된다.
    # 예) n = 15 / 승: 5 => n = 10이 되었으므로 승우 승

    # 항상 최선의 수만 둔다고 했으므로 자신의 차례에 돌을 가져가 남은 돌의 수가 10의 배수를 만든 사람이 이기게 된다.







