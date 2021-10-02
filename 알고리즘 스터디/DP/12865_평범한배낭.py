import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())    # 물품의 수 n, 버틸 수 있는 무게 k
arr = [list(map(int, input().split())) for _ in range(n)]    # [물건의 무게, 물건의 가치]
arr.sort()

dp = [0 for _ in range(100)]
dp_v = [0 for _ in range(100)]

for thing in arr:
    w = thing[0]    # 물건의 무게 w
    v = thing[1]    # 물건의 가치 v
    # dp[w] = max(dp[w], v)
    for i in range(w, k-w+1):
        dp[i] = max(v, dp[i-1])

print(dp)
print(dp[k])

