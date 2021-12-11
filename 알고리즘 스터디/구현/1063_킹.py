import sys
sys.stdin = open('input.txt')

# 명령에 따른 움직임
def move(command):
    if command == 'R':
        return (1, 0)
    elif command == 'L':
        return (-1, 0)
    elif command == 'B':
        return (0, -1)
    elif command == 'T':
        return (0, 1)
    elif command == 'RT':
        return (1, 1)
    elif command == 'LT':
        return (-1, 1)
    elif command == 'RB':
        return (1, -1)
    else:
        return (-1, -1)


king_point, rock_point, n = input().split() # 킹의위치, 돌 위치, 킹 움직인 횟수 n
kp_x, kp_y = ord(king_point[0]), int(king_point[1]) # 킹의 위치 x, y 분리
rp_x, rp_y = ord(rock_point[0]), int(rock_point[1]) # 돌의 위치 x, y 분리
king_move = [input() for _ in range(int(n))]    # 킹이 어떻게 움직여야 하는지 리스트로 받기

for command in king_move:
    x, y = move(command)    # 움직인 명령 받기
    nx = kp_x + x   # 명령 받은대로 위치 이동
    ny = kp_y + y
    if 65 <= nx <= 72 and 1 <= ny <= 8: # 움직일 위치가 체스판 범위 내에 있다면
        if rp_x == nx and rp_y == ny:   # 근데 돌의 위치랑 같아 졌다면
            if 65 <= rp_x + x <= 72 and 1 <= rp_y + y <= 8: # 돌을 왕이 움직인 대로 움직이고, 그 위치가 체스판 내라면
                kp_x, kp_y = nx, ny             # 왕 이동
                rp_x, rp_y = rp_x + x, rp_y + y # 돌 이동
        else:
            kp_x, kp_y = nx, ny # 돌 위치랑 안같다면 왕만 이동


print(chr(kp_x) + str(kp_y))    # 킹 마지막 위치
print(chr(rp_x) + str(rp_y))    # 돌 마지막 위치