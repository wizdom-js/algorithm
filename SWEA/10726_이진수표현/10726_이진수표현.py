import sys
sys.stdin = open("input.txt")


tc = int(input())
for idx in range(1, tc+1):
    n, m = map(int, input().split())

    # n번만큼 반복해서 조사할건데 한번이라도 0 나오면 off
    for i in range(n):
        # m의 i번째 비트가 1인지 아닌지 검사
        if m & (1 << i) == 0:   # 0이면 off
            print('#{} {}'.format(idx, 'OFF'))
            break
    else:
        print('#{} {}'.format(idx, 'ON'))