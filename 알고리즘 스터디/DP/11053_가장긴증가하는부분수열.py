import sys
sys.stdin = open('input.txt')

n = int(input())    # 수열의 크기
numbers = list(map(int, input().split()))   # 수열

p = 0
cnt = 0
for num in numbers:
    if p < num:
        p = num
        cnt += 1

print(cnt)