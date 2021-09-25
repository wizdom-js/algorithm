import sys
sys.stdin = open('input.txt')

tc = int(input())

for _ in range(tc):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]


    dp = [[0 for _ in range(n)] * 2 ]
