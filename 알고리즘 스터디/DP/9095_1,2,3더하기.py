import sys
sys.stdin = open('input.txt')

tc = int(input())
dp_l = [0, 1, 2, 4] + [0 for _ in range(9)]     # 11까지의 방법을 담을 리스트

# 규칙 : 정수 n을 1, 2, 3으로 나타낼 수 있는 방법 수 = 정수 n-3 , n-2, n-1 을 나타낼 수 있는 방법 수를 다 더한 것
# dp 함수
def dp(n):
    # 리스트에 현재 n을 나타낼 수 있는 방법의 수가 비어 있다면
    if not dp_l[n]:
        # 정수 n-1의 방법의 수가 저장되어 있는지 확인 -> 안되어있다면 또 들어감
        dp(n-1)
        # n-1까지 다 저장되어 있으면 현재 n의 정수를 나타낼 수 있는 방법의 수 저장.
        dp_l[n] = dp_l[n-3] + dp_l[n-2] + dp_l[n-1]


for i in range(tc):
    n = int(input())
    dp(n)
    print(dp_l[n])