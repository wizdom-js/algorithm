import sys
sys.stdin = open('input.txt')


n = int(input())

answer = [0 for _ in range(10000)]
answer[2] = 3
answer[3] = 5

for i in range(4, n+1):
    answer[i] = (answer[i-1] + 2 * answer[i-2]) % 10007
print(answer[n])