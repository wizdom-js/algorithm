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

h, w = map(int, input().split())    # 세로 길이 h, 가로 길이 w
blocks_h = list(map(int, input().split()))  # 블록의 높이들

l = 0   # 왼쪽 포인터
r = w-1 # 오른쪽 포인터

max_l = max_r = 0   # 왼쪽, 오른쪽의 각 블록의 최대 높이를 저장할 변수
rainwater = 0   # 고이는 빗물의 총량
while l < r:
    # 각 블록의 최대 높이 갱신
    max_l = max(max_l, blocks_h[l])
    max_r = max(max_r, blocks_h[r])

    if max_l < max_r:   # 오른쪽 블럭이 더 큰 경우
        rainwater += max_l - blocks_h[l]    # 왼쪽 블럭을 기준으로 빗물 계산
        l += 1
    else:               # 왼쪽 블럭이 더 큰 경우
        rainwater += max_r - blocks_h[r]    # 오른쪽 블럭을 기준으로 빗물 계산
        r -= 1

print(rainwater)