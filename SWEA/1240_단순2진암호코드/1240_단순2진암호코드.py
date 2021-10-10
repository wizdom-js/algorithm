import sys
sys.stdin = open('input.txt')


code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

tc = int(input())
for idx in range(1, tc+1):
    n, m = map(int, input().split())

    # 배열 받아오기
    arr = []
    binary = ''
    for n in range(n):
        temp = input()
        arr.append(temp)
        if not binary and '1' in temp:   # 2진수가 있는 배열 저장
            binary = temp

    p = m - binary[::-1].index('1') # 배열에서 마지막 1 찾기 (암호는 다 1로 끝남)
    binary = binary[p-56:p] # 2진수 범위만 딱 저장. 불필요한거 버려
    number = []
    for i in range(0, 56, 7):
        number.append(code[binary[i:i+7]])  # 암호코드에 맞는 번호 저장

    odd = 0     # 홀수 자리 합 저장
    even = 0    # 짝수 자리 합 저장
    for i in range(8):
        # 검증코드
        if i == 7:
            if (odd * 3 + even + number[i]) % 10 == 0:  # 정상적인 암호코드면
                print('#{} {}'.format(idx, odd + even + number[i]))  # 암호코드들의 숫자 합 출력
            else:   # 비정상 적이면
                print('#{} {}'.format(idx, 0))  # 0 출력
        # 짝수자리 더하기
        elif i % 2:
            even += number[i]
        # 홀수자리 더하기
        else:
            odd += number[i]


