import sys
sys.stdin = open('input.txt')

# (0, 0)에서 (1, 2)가 보이고 (2, 4), (3, 6)과 같은 좌표는 (1, 2)에 가려져서 보이지 않는다.
# 따라서 최대 공약수가 1인 경우에만 (0, 0)좌표에서 보인다.

# 최대 공약수 구하기
def get_GCD(a, b):
    while a % b != 0:
        a, b = b, a % b

    return b

# dp 풀이
# dp에 값들 먼저 다 저장해놓고 꺼내 쓰는 방식
dp = [0 for _ in range(1001)]
dp[1] = 3
for i in range(2, 1001):
    cnt = 0
    for j in range(1, i+1):
        if i == j: continue

        if get_GCD(i, j) == 1:
            cnt += 2    # 예) (2, 3) 와 (3, 2)
    dp[i] = dp[i - 1] + cnt # 이전 점들의 개수 + 추가된 점의 개수

testcase = int(input())
for _ in range(testcase):
    n = int(input())
    print(dp[n])


# 처음 풀이 (구현) => 시간초과
'''
testcase = int(input())
arr = [[0 for _ in range(1001)] for _ in range(1001)]
for _ in range(testcase):
    n = int(input())
    answer = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j]:
                continue

            if get_GCD(i, j) == 1:
                answer += 1
                # 배수에 해당되는 좌표들 처리하기 
                for k in range(1, 1000):
                    if i * k > 1000 or j * k > 1000:
                        break

                    arr[i*k][j*k] = True

    # for i in range(11):
    #     print(*arr[i])

    print(answer+2)
'''
