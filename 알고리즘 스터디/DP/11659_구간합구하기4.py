import sys
sys.stdin = open('input.txt')


input = sys.stdin.readline

n, m = map(int, input().split()) # 수의 개수 n, 합을 구해야 하는 횟수 m
numbers = list(map(int, input().split())) # n개의 수

# dp 리스트 만들기
dp = [0 for _ in range(n+1)]
for i in range(n):
    dp[i+1] = dp[i] + numbers[i]

for _ in range(m):
    i, j = map(int, input().split())

    print(dp[j] - dp[i-1])  # 구간 합