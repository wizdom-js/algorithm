import sys
sys.stdin = open('input.txt')

import heapq

n = int(input())    # 카드 묶음 수

# 입력받은 카드 묶음 정렬 - 1. 힙으로 정렬
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)

# 입력받은 카드 묶음 정렬 - 2. sorted
# cards = sorted([int(input()) for _ in range(n)])

answer = 0
while len(cards) > 1:   # 카드 비교 할 수 없을 때까지 반복
    n1 = heapq.heappop(cards)   # 카드리스트에서 가장 작은 카드 묶음 꺼내기
    n2 = heapq.heappop(cards)   # 그다음으로 작은 카드 묶음 꺼내기
    heapq.heappush(cards, n1 + n2)  # 두 카드 묶음 합을 카드리스트 크기에 맞게 넣기
    answer += n1 + n2   # 카드 비교 횟수 더해주기

print(answer)