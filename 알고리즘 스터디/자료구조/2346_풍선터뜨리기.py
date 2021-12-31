import sys
sys.stdin = open('input.txt')
#
# n = int(input())    # 풍선의 개수
# papers = list(map(int, input().split()))    # 풍선 안의 종이에 적혀 있는 수
#
# p = papers[0]
# cnt = 0
# move = 0
# direction = True
# print(1, end=' ')
# papers[0] = 0
# while cnt < n:
#     if papers[p] == 0 and cnt > 0:
#         if direction:
#             p += 1
#         else:
#             p -= 1
#     else:
#
#         print(p + 1, end=' ')
#
#         cnt += 1
#         move = papers[p]
#         direction = True if move > 0 else False
#         papers[p] = 0
#         p += move
#         if p < 0:
#             p += n
#         else:
#             p %= n






# n = int(input())    # 풍선의 개수
# papers = list(map(int, input().split()))    # 풍선 안의 종이에 적혀 있는 수
#
# p = cnt = move = 0
# direction = True
# while cnt < n:
#     if papers[p] == 0:
#         if direction:
#             p += 1
#         else:
#             p -= 1
#     else:
#         print(p + 1, end=' ')
#
#         cnt += 1
#         move = papers[p]
#         direction = True if move > 0 else False
#         papers[p] = 0
#         p += move
#     p = num(p)



n = int(input())     # 풍선의 개수
papers = list(enumerate(map(int, input().split()))) # 풍선 안의 종이에 적혀 있는 수

p = 1
move = 0
while n:
    p += move
    if move < 0:
        p %= n
    else:
        p = (p - 1) % n
    idx, move = papers.pop(p)
    n -= 1
    print(idx + 1, end=' ')






