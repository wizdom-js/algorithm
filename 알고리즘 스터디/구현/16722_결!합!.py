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

def hab(n1, n2, n3):
    global score
    for i in range(3):
        if board[n1][i] == board[n2][i] != board[n3][i]:
            continue
        elif board[n1][i] != board[n2][i] == board[n3][i]:
            continue
        elif board[n1][i] != board[n3][i] == board[n2][i]:
            continue
        else:
            score += 1


board = [[0, 0, 0] for _ in range(10)]

for i in range(9):
    s, c, b = input().split()
    input_board(i, s, c, b)


hab_comb = {}
for i in range(1, 8):
    for j in range(i+1, 9):
        for k in range(j+1, 10):
            for z in range(3):
                if board[i][z] == board[j][z] != board[k][z]:
                    break
                elif board[i][z] != board[j][z] == board[k][z]:
                    break
                elif board[i][z] != board[j][z] == board[k][z]:
                    break
            else:
                tmp = str(i) + str(j) + str(k)
                hab_comb[tmp] = False

game_n = int(input())
score = 0
record = {}
print(hab_comb)
for _ in range(game_n):
    player = input()
    print('------', player)
    if player[0] == "H":
        tmp = sorted(player[1:].split())
        cards = ''.join(tmp)
        print(cards)
        if cards in hab_comb and not hab_comb[cards]:
            hab_comb[cards] = True
            print("true")
            score += 1
        else:
            print("false")
            score -= 1
    else:
        for value in hab_comb.values():
            if not value:
                score -= 1
                break
        else:
            score += 1

print(score)
