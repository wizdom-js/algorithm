import sys
sys.stdin = open('input.txt')

# 최대공약수 구하기
def gcd(n1, n2):
    while n1 % n2 != 0:
        n1, n2 = n2, n1 % n2
    return n2


N1, N2 = map(int, input().split())

ans1, ans2 = N1, N2     # 정답 변수에 두 수 담기 (서로소인경우 그대로 반영)
s = N2 // N1 // N1
temp1, temp2 = N1*s, N2//s
print(temp1, temp2)
for i in range(1, s):
    n1 = temp1 // i
    n2 = temp2 * i

    temp = gcd(n1, n2)  # n1, n2의 최대 공약수 저장
    if N1 == temp and N2 == (n1 * n2 // temp):  # 목표한 최대 공약수와 최소공배수면 갱신
        ans1, ans2 = n1, n2
        break

print(ans1, ans2)