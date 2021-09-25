import sys
sys.stdin = open('input.txt')


n = int(input())    # 수열의 크기
numbers = list(map(int, input().split()))   # 수열

dp = [0 for _ in range(n)]  # dp 배열
answer = -1001  # 주어진 수열의 원소 범위보다 더 작게 설정

for i in range(n):
    dp[i] = max(dp[i-1] + numbers[i], numbers[i]) # 이전까지의 연속 합 vs 현재 숫자 (현재 숫자 택하면 꼬리자르기)
    answer = max(dp[i], answer) # 현재까지의 합이 더 크다면 answer 갱신

print(answer)