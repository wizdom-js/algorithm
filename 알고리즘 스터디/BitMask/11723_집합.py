import sys
sys.stdin = open('input.txt')

m = int(sys.stdin.readline())    # 수행해야 하는 연산의 수
s = 0   # 비어있는 공집합 s
for i in range(m):
    command = sys.stdin.readline().split()
    if command[0] == 'all': # S를 {1, 2, ..., 20} 으로 바꾼다.
        s = (1 << 21) - 1   # 0b11111111111111111111
    elif command[0] == 'empty': # 공집합으로 바꾼다.
        s = 0
    else:
        command, n = command[0], int(command[1])    # 명령어, 숫자 x
        if command == 'add':    # n 추가
            s |= (1 << n)
        elif command == 'remove':   # n 제거
            s &= ~(1 << n)
        elif command == 'check':    # n이 있으면 1, 없으면 0 출력
            print(1 if s & (1 << n) else 0)
        elif command == 'toggle':   # n이 있으면 n 제거, 없으면 n 추가
            s ^= (1 << n)

