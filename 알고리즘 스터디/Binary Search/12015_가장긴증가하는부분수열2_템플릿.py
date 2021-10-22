import sys
sys.stdin = open('input.txt')


n = int(input())
arr = list(map(int, input().split()))
dp = [1 for i in range(20)]
prv = [-1 for i in range(20)]
answer = 0
idx = 0

for i in range(n):
    for j in range(i):
        if arr[i] <= arr[j]:
            continue

        if dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prv[i] = j

        print('dp ##########')
        print(dp)
        print('prv ##############')
        print(prv)

print('----------------------------')
for i in range(n):
    if answer < dp[i]:
        answer = dp[i]
        idx = i
        print('answer:', answer, 'idx', idx)

print('----------------------------')
print(dp)
print(answer)
while idx >= 0:
    print(arr[idx])
    idx = prv[idx]
    print('idx:', idx)