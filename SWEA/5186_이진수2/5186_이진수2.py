import sys
sys.stdin = open("sample_input.txt")


tc = int(input())
for idx in range(1, tc+1):
    n = float(input())

    cnt = 0     # 자리 수 count
    binary = '' # 2진수 저장
    while n > 0:
        temp = n * 2
        binary += str(temp)[0]  # 정수부분 저장
        n = temp - int(temp)    # 소수점 이하 저장
        cnt += 1

        if cnt > 12:    # 13자리 이상이면 중단
            break

    if cnt > 12:    # 13자리 이상이면 overflow 출력
        print('#{} {}'.format(idx, 'overflow'))
    else:
        print('#{} {}'.format(idx, binary))
