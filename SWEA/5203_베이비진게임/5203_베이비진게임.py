import sys
sys.stdin = open('sample_input.txt')


# babygin인지 확인하는 함수
def is_babygin(p_cards, n):
    for i in range(n-2):
        if p_cards[i] + 1 in p_cards and p_cards[i] + 2 in p_cards: # run 인가요 ?
            return True
        elif p_cards[i] == p_cards[i+1] == p_cards[i+2]:    # triplet 인가요?
            return True
    return False    # 암것도 아니야


for idx in range(1, int(input())+1):
    cards = list(map(int, input().split()))

    player1 = []
    player2 = []
    answer = 0
    for i in range(0, 12, 2):
        player1.append(cards[i])
        player2.append(cards[i + 1])

        if 4 <= i:
            # player1 카드 검토
            if is_babygin(sorted(player1), i//2+1):
                answer = 1  # triplet이나 run 됐으면 갱신하고 승자 출력
                break

            # player2 카드 검토
            if is_babygin(sorted(player2), i//2+1):
                answer = 2
                break

    print('#{} {}'.format(idx, answer)) # 둘다 babygin 되지 못했으면 0(무승부) 출력