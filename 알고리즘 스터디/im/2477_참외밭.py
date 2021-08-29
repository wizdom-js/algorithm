import sys
sys.stdin = open('input.txt')

# n = int(input())
#
# field = [0 for _ in range(5)]   # 방향에 따라 받을 길이
# minus = []  # 참외밭에서 빈곳 빼주기 위한 길이 담을 거.
#
# for _ in range(6):
#     i, l = map(int, input().split())    # 방향,  길이
#
#     # 만약 이미 해당 방향에 길이가 저장되어 있다면
#     # 길이가 더 작은 것을 minus에 저장한다.
#     if field[i]:
#         if field[i] < l:
#             minus.append(field[i])
#         else:
#             minus.append(l)
#     else:
#         field[i] = l
#
# # 큰 사각형 길이 구하기
# w = field[2] if field[1] < field[2] else field[1]
# h = field[4] if field[3] < field[4] else field[3]
#
# # 큰 사각형에서 작은 사각형 빼기
# print(w*h*n - minus[0]*minus[1]*n)


n = int(input())
l = [int(input().split()[1]) for _ in range(6)]  # 길이들 담기

# 큰 직사각형의 참외 밭에서, 작은 직사각형 (참외밭이 아닌곳)을 빼주는 형식
# 뺴줄 직사각형의 길이 두개는 큰 사각형의 길이 중 작은 것에서 세칸 이동하면 나온다.
# 반 시계 방향이고, 밭이 이어져 있으니
# (큰 사각형의 작은 길이  -> 큰 사각형의 큰 길이 -> 다른 변 -> 다른 변 -> 작은 사각형 길이1 -> 작은 사각형 길이2) 순이 되기 때문이다.

# idx = field.index(max(field))   # 가장 긴 길이 인덱스 구하기
# 위처럼 하면 큰 사각형의 길이가 두개일때 (정사각형일때) 구할 수 없다.

# 따라서 크기를 비교해서 가장 큰 크기의 인덱스를 저장하기로 한다.
big_s = 0
idx = 0
for i in range(6):
    temp = l[i] * l[(i+1)%6]    # 크기 구하기
    if big_s < temp:      # 기존 크기보다 크다면 갱신, 인덱스 저장
        big_s = temp
        idx = i

# 큰 직사각형에서 작은 직사각형 빼기
final_f = (big_s - (l[(idx+3) % 6] * l[(idx+4) % 6]))
print(final_f * n)  # 참외의 수


