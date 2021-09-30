import sys
sys.stdin = open("sample_input.txt")



tc = int(input())
for idx in range(1, tc+1):
    binary = input()
    ternary = input()

    guess_bin = []  # 2진수로 만들 수 있는 경우의 수 다 넣기
    for i in range(len(binary)):
        if binary[i] == '0':    # 해당 자리 0이었으면 1로 바꾸고 10진수 변환해서 리스트에 넣기
            change = binary[:i] + '1' + binary[i+1:]
            guess_bin.append(int(change, 2))
        else:                   # 해당 자리 1이었으면 0로 바꾸고 10진수 변환해서 리스트에 넣기
            change = binary[:i] + '0' + binary[i + 1:]
            guess_bin.append(int(change, 2))

    ter = '012' # 3진수로 사용할 숫자
    for i in range(len(ternary)):
        for j in ter:
            if ternary[i] == j: # 원래 숫자이면 넘어가
                continue
            # 해당 자리(i)의 숫자 바꿔서 10진수로 변환
            change = int(ternary[:i] + j + ternary[i + 1:], 3)
            if change in guess_bin: # 변환한 숫자가 2진수로 만든 숫자중에 있는지 확인
                print('#{} {}'.format(idx, change)) # 있으면 출력하고 중단
                break
