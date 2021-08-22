import sys
sys.stdin = open('input.txt')

n = int(input())
time = sorted(list(map(int, input().split())))

min_time = 0
temp = 0
for t in time:
    min_time += temp + t
    temp += t

print(min_time)

