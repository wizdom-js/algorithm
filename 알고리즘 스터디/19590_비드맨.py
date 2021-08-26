import sys
sys.stdin = open('input.txt')

########### 파이파이 ########

input = sys.stdin.readline

n = int(input())
guseul = [int(input()) for _ in range(n)]

many_g = max(guseul)       # 가장 많은 구슬 가져오기
sum_guseul = sum(guseul)    # 구슬들의 합

if n == 1:
    print(many_g)
    exit()

# 가장 많은 구슬이 나머지 구슬보다 많다면 걍 깨
if many_g >= sum_guseul-many_g:
    print(sum_guseul - many_g)
    exit()

# 나머지 구슬들이 더 많으면
else:
    # 나머지 구슬의 합과 젤 많은 구슬의 차가 짝수이면 무조건 다 깨짐. 홀수이면 1개 남음
    answer = 1 if sum_guseul % 2 else 0
    print(answer)




# ###########
# n = int(input())
# guseul = sorted([int(input()) for _ in range(n)])
#
# many_g = guseul.pop()       # 가장 많은 구슬 가져오기
# sum_guseul = sum(guseul)    # 많은 구슬 제외한 나머지 구슬들의 합
#
# # 가장 많은 구슬이 나머지 구슬보다 많다면 걍 깨
# if many_g >= sum_guseul:
#     many_g -= sum_guseul
#
# # 나머지 구슬들이 더 많으면
# else:
#     # 나머지 구슬의 합과 젤 많은 구슬의 차가 짝수이면 무조건 다 깨짐. 홀수이면 1개 남음
#     many_g = 1 if (sum_guseul - many_g) % 2 else 0
#
# print(many_g)