import sys
sys.stdin = open('input.txt')


tc = int(input())
for tc_n in range(1, tc+1):
    n = int(input())
    coordinate = [[0, 0] for _ in range(n+2)]
    for i in range(n+2):
        coordinate[i] = list(map(int, input().split()))

        