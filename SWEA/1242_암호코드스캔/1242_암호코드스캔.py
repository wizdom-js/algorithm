import sys
sys.stdin = open("sample_input.txt")


# 맨 앞 0까지 비율 하면 복잡해서 빼줌
ratio = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}


tc = int(input())
for idx in range(1, tc+1):
    n, m = map(int, input().split())    # 세로 크기 n, 가로 크기 m
    arr = list(set([input() for _ in range(n)]))    # 중복제거
    arr = sorted(arr)[1:]   # 0만 있는 배열 제거

    numbers = []    # 암호 넣는 리스트
    answer = 0
    for p in arr:
        # 1. 16진수 -> 2진수 변환
        # 2. 왼쪽 0 다 제거
        # 3. 마지막에 0 붙이기 (마지막 자리를 위해)
        binary = format(int(p, 16), 'b').lstrip('0') + '0'
        n1 = n2 = n3 = 0    # 각 비율을 담을 변수
        cnt = 0  # 암호 8자리 count
        odd = 0  # 홀수 자리 합 저장
        even = 0  # 짝수 자리 합 저장
        temp = ''
        for i in range(len(binary)):
            if binary[i] == '1' and n2 == 0:    # 첫번째 1 비율
                n1 += 1
            elif binary[i] == '0' and n1 != 0 and n3 == 0:  # 두번째 0 비율
                n2 += 1
            elif binary[i] == '1' and n2 != 0:  # 세번째 1 비율
                n3 += 1
            elif n3 != 0:   # 비율 다 구한 경우
                cnt += 1
                r = min(n1, n2, n3) # 가장 작은 숫자 구하기 (비율 구하기 위함)
                pw = ratio[(n1//r, n2//r, n3//r)]   # 암호 가져오기
                temp += str(pw)
                # 마지막 번호인 경우
                if cnt == 8:
                    if (odd * 3 + even + pw) % 10 == 0 and temp not in numbers:  # 정상적인 암호코드이고 했던거 아니라면
                        answer += odd + even + pw   # 값 더해주기
                    numbers.append(temp)    # 해당 암호 저장
                    odd = even = cnt = 0    # 변수들 초기화
                    temp = ''
                # 8번째 자리 이전의 숫자인 경우
                elif cnt % 2:
                    odd += pw   # 홀수 자리 더하기
                else:
                    even += pw  # 짝수 자리 더하기

                n1 = n2 = n3 = 0    # 비율 변수 초기화

    print('#{} {}'.format(idx, answer))


# print(bin(int('1E06079861E79F99FE079861E79F', 16)))