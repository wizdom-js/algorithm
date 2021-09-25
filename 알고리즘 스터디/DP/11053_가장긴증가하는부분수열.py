import sys
sys.stdin = open('input.txt')

n = int(input())    # 수열의 크기
numbers = list(map(int, input().split()))   # 수열

dp = [1 for _ in range(n)] # dp 배열 만들기 (자기자신 1이니까 1로 초기화)
answer = 1  # 가장 긴 증가하는 부분 수열 길이

for i in range(n):
    for j in range(i):  # 현재 위치(i)보다 전의 숫자(j)가 작은지 확인
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j]+1)  # 결국 i위치의 이전 길이중 최댓값에 +1 하게 된다
            answer = max(dp[i], answer)  # 가장 긴 이라고 했으니, 길어졌다면 큰 값으로 갱신

print(answer)