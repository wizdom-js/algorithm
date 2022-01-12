import sys
sys.stdin = open('input.txt')

tc = int(input())
for _ in range(tc):
    n = int(input())
    logs = sorted(list(map(int, input().split())))

    arrange_logs = [0 for _ in range(n)]
    for i in range(n):
        if i % 2:
            arrange_logs[-(i // 2) - 1] = logs[i]
        else:
            arrange_logs[i // 2] = logs[i]

    answer = 0
    for i in range(n):
        answer = max(answer, abs(arrange_logs[i-1] - arrange_logs[i]))

    print(answer)

