import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
numbers = [list(map(int, input().split())) for _ in range(n)]

prefix_sum = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + numbers[i-1][j-1]

answer = -9999999999999
for x1 in range(1, n+1):
    for y1 in range(1, n+1):
        for x2 in range(x1, n+1):
            for y2 in range(y1, n+1):
                answer = max(answer, prefix_sum[y2][x2] + prefix_sum[y1-1][x2] - prefix_sum[y2][x1-1] - prefix_sum[y1-1][x1-1])

print(answer)