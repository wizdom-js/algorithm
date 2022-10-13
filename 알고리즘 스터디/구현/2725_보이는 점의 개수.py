import sys
sys.stdin = open('input.txt')

def get_GCD(a, b):
    while a % b != 0:
        a, b = b, a % b

    return b

# dp 풀이
dp = [0 for _ in range(1001)]
dp[1] = 3
for i in range(2, 1001):
    cnt = 0
    for j in range(1, i+1):
        if i == j: continue

        if get_GCD(i, j) == 1:
            cnt += 2
    dp[i] = dp[i - 1] + cnt

testcase = int(input())
for _ in range(testcase):
    n = int(input())
    print(dp[n])


# 처음 풀이 (구현)
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
                for k in range(1, 1000):
                    if i * k > 1000 or j * k > 1000:
                        break

                    arr[i*k][j*k] = True

    # for i in range(11):
    #     print(*arr[i])

    print(answer+2)
'''
