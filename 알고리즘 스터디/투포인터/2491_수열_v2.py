import sys
sys.stdin = open('input.txt')

########### 투포인터 #########

# 최종버전 # 영남이오빠 코드

n = int(input())
numbers = list(map(int, input().split()))

big = small = 0
max_l = 0

for i in range(1, n):
    if numbers[i-1] <= numbers[i]:
        big += 1
    else:
        big = 0

    if numbers[i] <= numbers[i-1]:
        small += 1
    else:
        small = 0

    max_l = max(max_l, big, small)

print(max_l + 1)



# 이게 더 시간 짧음

# n = int(input())    # 숫자의 개수
# numbers = list(map(int, input().split()))   # 숫자들
#
# bs = be = ss = se = 0   # 연속해서 커지는 경우와 작아지는 경우의 시작, 끝 포인트 각각 설정
# max_l = 0   # 최대 길이 받을 변수
#
# for i in range(1, n):
#     # 현재 숫자(i)가 이전 숫자보다 더 크거나 같은 경우 -> 연속해서 커지는 경우
#     if numbers[be] <= numbers[i]:
#         be += 1    # 구간 한칸 늘리기
#     else:
#         if max_l < be - bs:   # 범위가 길어졌다면 갱신
#             max_l = be - bs
#         bs = be = i    # 연속하지 않는 경우 시작과 끝 포인트 다시 설정
#
#     # 현재 숫자(i)가 이전 숫자보다 더 작거나 같은 경우 -> 연속해서 작아지는 경우
#     if numbers[i] <= numbers[se]:
#         se += 1
#     else:
#         if max_l < se - ss:
#             max_l = se - ss
#         ss = se = i
#
# # 마지막 숫자도 연속 됐을 수 있잖아 ? 확인
# if max_l < be - bs:
#     max_l = be - bs
# if max_l < se - ss:
#     max_l = se - ss
#
# print(max_l + 1)    # 숫자 하나가 구간의 길이 1이므로 +1해준다.
#
#
#
# ######################################################
#
# def not_straight(s, e, max_l):
#
#     if max_l < e - s:   # 범위가 길어졌다면 갱신
#         max_l = e - s
#
#     return max_l
#
#
#
# n = int(input())    # 숫자의 개수
# numbers = list(map(int, input().split()))   # 숫자들
#
# bs = be = ss = se = 0   # 연속해서 커지는 경우와 작아지는 경우의 시작, 끝 포인트 각각 설정
# max_l = 0   # 최대 길이 받을 변수
#
# for i in range(1, n):
#     # 현재 숫자(i)가 이전 숫자보다 더 크거나 같은 경우 -> 연속해서 커지는 경우
#     if numbers[be] <= numbers[i]:
#         be += 1    # 구간 한칸 늘리기
#     else:
#         max_l = not_straight(bs, be, max_l)
#         bs = be = i  # 연속하지 않는 경우 시작과 끝 포인트 다시 설정
#
#     # 현재 숫자(i)가 이전 숫자보다 더 작거나 같은 경우 -> 연속해서 작아지는 경우
#     if numbers[i] <= numbers[se]:
#         se += 1
#     else:
#         max_l = not_straight(ss, se, max_l)
#         ss = se = i
#
# max_l = not_straight(bs, be, max_l)
# max_l = not_straight(ss, se, max_l)
#
print(max_l + 1)    # 숫자 하나가 구간의 길이 1이므로 +1해준다.