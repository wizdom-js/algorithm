import sys
sys.stdin = open('input.txt')

import heapq

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)

# cards = sorted([int(input()) for _ in range(n)])

answer = 0
while len(cards) > 1:
    n1 = heapq.heappop(cards)
    n2 = heapq.heappop(cards)
    heapq.heappush(cards, n1 + n2)
    answer += n1 + n2

print(answer)