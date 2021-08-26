import sys
sys.stdin = open('input.txt')

n = int(input())
time = sorted(list(map(int, input().split())))  # 걸리는 시간 작은 순으로 정렬 (그게 이득)

min_time = 0
temp = 0
for t in time:
    min_time += temp + t
    temp += t

print(min_time)

