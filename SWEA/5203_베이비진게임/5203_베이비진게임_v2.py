import sys
sys.stdin = open('sample_input.txt')


# run인지 확인하는 함수
def is_run(p_cards):
    for i in range(8):
        if p_cards[i] > 0 and p_cards[i+1] > 0 and p_cards[i+2] > 0:    # 연속된 세 자리에 각 카드가 하나 이상 있나요?
            return True
    return False    # run 아니야


for idx in range(1, int(input())+1):
    cards = list(map(int, input().split()))

    player1 = [0 for _ in range(10)]
    player2 = [0 for _ in range(10)]
    answer = 0
    for i in range(0, 12, 2):
        player1[cards[i]] += 1      # 해당 인덱스에 +1
        player2[cards[i+1]] += 1

        if 4 <= i:
            # player1 카드 검토
            if player1[cards[i]] == 3 or is_run(player1):   # triplet이나 run 됐으면 갱신하고 승자 출력
                answer = 1
                break

            # player2 카드 검토
            if player2[cards[i+1]] == 3 or is_run(player2):
                answer = 2
                break

    print('#{} {}'.format(idx, answer)) # 둘다 babygin 되지 못했으면 0(무승부) 출력