import sys
sys.stdin = open("sample_input.txt")

# 16진수 -> 2진수
def hex_to_bin(hexa):
    binary = ''
    for i in hexa:
        x = int(i, 16)  # 10진수 변환
        temp = ''
        # 10진수 -> 2진수 변환
        for _ in range(4):
            x, n = divmod(x, 2)
            temp = str(n) + temp
        binary += temp
    return binary

def hex_to_bin2(n, hexa):
    x = int(hexa, 16)
    for j in range(n-1, -1, -1):
        if x & (2 ** j) == 0:
            print(0, end='')
        else:
            print(1, end='')
    print()



tc = int(input())
for idx in range(1, tc+1):
    n, hexa = input().split()

    print('#{} {}'.format(idx, hex_to_bin(hexa)))

    print('#{} {}'.format(idx, bin(int(hexa, 16))[2:].zfill(int(n)*4)))   # 내장함수 bin 사용

    print('#{} {}'.format(idx, format(int(hexa, 16), 'b').zfill(int(n)*4)))   # format 사용

    hex_to_bin2(int(n)*4, hexa) # 비트연산자 사용

