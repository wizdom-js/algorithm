import sys
sys.stdin = open('input.txt')

# tc 수
tc = int(input())

# tc 수만큼 반복
for idx in range(1, tc+1):
    # 카드 장수 n
    n = int(input())
    # n개의 숫자 cards
    cards = int(input())
    # 카드 개수가 들어갈 리스트
    cards_count = [0 for i in range(10)]

    # 카드가 담긴 cards를 돌며 카드 개수 세기
    for i in range(n):
        # 나머지를 떼서 해당 인덱스(카드 수)에 저장
        cards_count[cards%10] += 1
        cards //= 10

    # 가장 많은 카드와 그 개수 초기화
    max_card = 0
    max_idx = 0
    for i in range(10):
        # 카드 개수가 저장되어 있는 값보다 크다면 그 카드의 인덱스(카드 숫자)와 개수를 저장한다.
        if cards_count[i] >= max_card:
            max_card = cards_count[i]
            max_idx = i

    print('#{} {} {}'.format(idx, max_idx, max_card))
