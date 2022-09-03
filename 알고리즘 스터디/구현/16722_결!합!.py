import sys
sys.stdin = open('input.txt')

def input_board(idx, s, c, b):
    if s == "TRIANGLE":
        board[idx][0] = 1
    elif s == "SQUARE":
        board[idx][0] = 2

    if c == "RED":
        board[idx][1] = 1
    elif c == "BLUE":
        board[idx][1] = 2

    if b == "WHITE":
        board[idx][2] = 1
    elif b == "BLACK":
        board[idx][2] = 2


board = [[0, 0, 0] for _ in range(10)]

for i in range(1, 10):
    s, c, b = input().split()
    input_board(i, s, c, b)

hab_comb = {}
for i in range(1, 8):
    for j in range(i+1, 9):
        for k in range(j+1, 10):
            for z in range(3):
                if board[i][z] == board[j][z] == board[k][z] or board[i][z] != board[j][z] != board[k][z] != board[i][z]:
                    continue
                else:
                    break
            else:
                tmp = str(i) + str(j) + str(k)
                hab_comb[tmp] = False

game_n = int(input())
score = 0
for _ in range(game_n):
    player = input()
    if player[0] == "H":
        tmp = sorted(player[1:].split())
        cards = ''.join(tmp)
        if cards in hab_comb and not hab_comb[cards]:
            hab_comb[cards] = True
            score += 1
        else:
            score -= 1
    else:
        for value in hab_comb.values():
            if not value:
                score -= 1
                break
        else:
            score += 3

print(score)
