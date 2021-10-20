import sys
sys.stdin = open('input.txt')


def binary_search(t_num):
    s = 0  # 시작, 마지막 포인트 초기화
    e = n1 - 1
    while s <= e:
        m = (s + e) // 2  # 중간지점 인덱스
        if number1[m] == t_num:  # 수첩 1에 숫자 있다면
            return 1
        elif number1[m] > t_num:  # 중간지점 값이 목표 숫자보다 크다면
            e = m - 1  # 시작 ~ 중간 범위 설정
        else:  # 중간지점 값이 목표 숫자보다 작다면
            s = m + 1  # 중간 ~ 끝 범위 설정
    return 0  # 수첩 1에 숫자 없는 경우


tc = int(input())
for _ in range(tc):
    n1 = int(input())    # 수첩 1에 적어놓은 정수의 개수
    number1 = sorted(set(map(int, input().split())))   # 수첩 1에 적힌 숫자들
    n1 = len(number1)

    n2 = int(input())   # 수첩 2에 적어놓은 정수의 개수
    number2 = list(map(int, input().split()))   # 수첩 2에 적힌 숫자들

    for t_num in number2:   # 수첩 2에 적혀있는 순서대로 수첩 1에 있는지 이진 탐색
        print(binary_search(t_num))

