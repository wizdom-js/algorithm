import sys
sys.stdin = open('input.txt')

# n, k, b = map(int, input().split())
# broken_light = [int(input()) for _ in range(b)]
#
# l = 0
# answer = float('inf')
# tmp = 0
# for i in range(1, n+1):
#     if i in broken_light:
#         tmp += 1

#     if i - l == k:
#         if tmp < answer:
#             answer = tmp
#         l += 1
#         if l in broken_light:
#             tmp -= 1
#

#
# print(answer)

n, k, b = map(int, input().split())
broken_light = [0 for _ in range(n+1)]
for _ in range(b):
    broken_light[int(input())] = 1

l = 0
answer = float('inf')
tmp = 0
for i in range(1, n+1):
    if broken_light[i]:
        tmp += 1

    if i - l == k:
        if tmp < answer:
            answer = tmp
        l += 1
        if broken_light[l]:
            tmp -= 1

print(answer)


n, k, b = map(int, input().split())
broken_light = [0 for _ in range(n+1)]
for _ in range(b):
    broken_light[int(input())] = 1

l = 0
answer = sum(broken_light[:k+1])
for i in range(1, n):
