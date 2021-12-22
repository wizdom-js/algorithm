import sys
sys.stdin = open('input.txt')

m = int(sys.stdin.readline())    # 수행해야 하는 연산의 수
s = 0
for i in range(m):
    command = sys.stdin.readline().split()
    if command[0] == 'all':
        s = (1 << 21) - 1
    elif command[0] == 'empty':
        s = 0
    else:
        command, n = command[0], int(command[1])
        if command == 'add':
            s |= (1 << n)
        elif command == 'remove':
            s &= ~(1 << n)
        elif command == 'check':
            print(1 if s & (1 << n) else 0)
        elif command == 'toggle':
            s ^= (1 << n)
print((1 << 21 )-1)
print(int(0b111111111111111111111))