import sys
sys.stdin = open('input.txt')

# 보드에 도형 숫자형태로 채워넣기
def input_board(idx, s, c, b):
    # 모양 - 0: 동그라미, 1: 세모, 2: 네모
    if s == "TRIANGLE":
        board[idx][0] = 1
    elif s == "SQUARE":
        board[idx][0] = 2

    # 색 - 0: 노랑, 1: 빨강, 2: 파랑
    if c == "RED":
        board[idx][1] = 1
    elif c == "BLUE":
        board[idx][1] = 2

    # 배경색 - 0: 회색, 1: 흰색, 2: 검은색
    if b == "WHITE":
        board[idx][2] = 1
    elif b == "BLACK":
        board[idx][2] = 2


board = [[0, 0, 0] for _ in range(10)]

for i in range(1, 10):
    s, c, b = input().split()
    input_board(i, s, c, b)

# 합이되는 조합 먼저 만들어 놓기
hab_comb = {}
for i in range(1, 8):
    for j in range(i+1, 9):
        for k in range(j+1, 10):
            for z in range(3):
                # 세 가지 속성이 모두 같거나 모두 다르다면 '합'
                if board[i][z] == board[j][z] == board[k][z] or board[i][z] != board[j][z] != board[k][z] != board[i][z]:
                    continue
                else:
                    break
            else:   # 합인 경우 조합 넣기
                tmp = str(i) + str(j) + str(k)
                hab_comb[tmp] = False

game_n = int(input())
score = 0
gyul_flag = False   # 결을 외쳤는지 확인하는 플래그
for _ in range(game_n):
    player = input()
    # 합을 외친 경우
    if player[0] == "H":
        tmp = sorted(player[1:].split())
        cards = ''.join(tmp)
        if cards in hab_comb and not hab_comb[cards]:
            hab_comb[cards] = True
            score += 1
        else:
            score -= 1
    # 결을 외친 경우
    else:
        for value in hab_comb.values():
            if not value:   # 외치지 않은 합이 있을 경우
                score -= 1
                break
        else:   # 외치지 않은 합이 없는 경우
            if not gyul_flag:
                score += 3
                gyul_flag = True
            else:
                score -= 1

print(score)
