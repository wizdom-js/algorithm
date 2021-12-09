import sys
sys.stdin = open('input.txt')


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


king_point, rock_point, n = input().split()
kp_x, kp_y = ord(king_point[0]), int(king_point[1])
rp_x, rp_y = ord(rock_point[0]), int(rock_point[1])
king_move = [input() for _ in range(int(n))]

for command in king_move:
    x, y = move(command)
    nx = kp_x + x
    ny = kp_y + y
    if 65 <= nx <= 72 and 1 <= ny <= 8:
        if rp_x == nx and rp_y == ny:
            if 65 <= rp_x + x <= 72 and 1 <= rp_y + y <= 8:
                kp_x, kp_y = nx, ny
                rp_x, rp_y = rp_x + x, rp_y + y
        else:
            kp_x, kp_y = nx, ny


print(chr(kp_x) + str(kp_y))
print(chr(rp_x) + str(rp_y))