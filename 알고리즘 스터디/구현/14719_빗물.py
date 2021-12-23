import sys
sys.stdin = open('input.txt')

#
# h, w = map(int, input().split())
# # blocks_h = list(map(int, input().split()))
# #
# # max_h = 0
# # max_h2 = 0
# # rainwater = 0
# # p = 0
# # for i in range(w):
# #     if max_h <= blocks_h[i]:
# #         max_h = blocks_h[i]
# #         max_h2 = 0
# #         p = 0
# #     else:
# #         if max_h2 < blocks_h[i]:
# #             max_h2 = blocks_h[i]
# #         rainwater += max_h - blocks_h[i]
# #         p += 1
# #
# # if max_h2:
# #     rainwater -= p * (max_h - max_h2)
# # print(rainwater)

# h, w = map(int, input().split())
# blocks_h = list(map(int, input().split()))
#
# max_h = 0
# max_h2 = 0
# rainwater = 0
# tmp = []
# for i in range(w):
#     if max_h <= blocks_h[i]:
#         for j in tmp:
#             rainwater += max_h - j
#         max_h = blocks_h[i]
#         tmp = []
#     else:
#         if max_h2 < blocks_h[i]:
#             max_h2 = blocks_h[i]
#         tmp.append(blocks_h[i])
#
# if tmp:
#     max_h2 = max(tmp)
#     ok = True
#     for j in tmp:
#         if j == max_h2: ok = not ok
#         if ok:
#             rainwater += max_h2 - j
# print(rainwater)

h, w = map(int, input().split())
blocks_h = list(map(int, input().split()))

l = 0
r = w-1

max_l = max_r = 0
rainwater = 0
while l < r:
    max_l = max(max_l, blocks_h[l])
    max_r = max(max_r, blocks_h[r])
    if max_l < max_r:
        rainwater += max_l - blocks_h[l]
        l += 1
    else:
        rainwater += max_r - blocks_h[r]
        r -= 1

print(rainwater)