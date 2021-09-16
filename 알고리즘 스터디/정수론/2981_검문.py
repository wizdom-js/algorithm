import sys
sys.stdin = open('input.txt')

import math

n = int(input()) # 종이에 적은 수의 개수

numbers = sorted([int(input()) for _ in range(n)], reverse=True)    # 내림차순 정렬

n1 = numbers[0]
gcd = 0
for i in range(n-1):
    n2 = n1 - numbers[i+1]  # 붙어있는 숫자의 차이

    # 이전 두 수의 차와 현재 두 수의 차의 최대공약수 구하기
    # ex) a-b와 b-c의 최대 공약수 구하기
    gcd = math.gcd(gcd, n2)

    n1 = numbers[i+1]   # 다음 숫자 차 구하기 위해 갱신

# 최종 최대 공약수의 약수 구하기
answer = []
for i in range(2, gcd+1):
    if i * i > gcd:
        break

    if gcd % i == 0:
        answer.append(i)
        if i * i != gcd:
            answer.append(gcd // i)
answer.sort()
print(*answer, gcd)

