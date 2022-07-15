import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())

numbers = [0 for _ in range(n+1)]

for i in range(2, n+1):
    if numbers[i]:
        continue
    for j in range(i, n+1, i):
        if not numbers[j]:
            numbers[j] = True
            k -= 1
            if k == 0:
                print(j)
                exit()