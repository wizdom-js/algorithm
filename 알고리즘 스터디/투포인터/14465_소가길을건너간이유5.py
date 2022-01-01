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

n, k, b = map(int, input().split()) # n번까지의 번호가 붙은 횡단보도, k개의 신호등, 부서진 신호등 개수 b
lights = [0 for _ in range(n+1)]  # 신호등 표시
for _ in range(b):
    lights[int(input())] = 1  # 부서진 신호등 1로 표시

l = 0
answer = float('inf')   # 최소 수리해야하는 신호등 개수
tmp = 0     # 수리해야하는 신호등 개수 임시로 담는 변수
for i in range(1, n+1):
    if lights[i]: # 부서진 신호등이라면 + 1
        tmp += 1

    if i - l == k:  # k 개수 충족됐다면
        if tmp < answer:    # 고칠 신호등 개수 최소로 갱신
            answer = tmp
        l += 1  # 다음 구역으로 넘어가기
        if lights[l]: # 이전 지점이 부서진 신호등이었다면
            tmp -= 1    # 빼주기

print(answer)


n, k, b = map(int, input().split())
lights = [0 for _ in range(n+1)]
for _ in range(b):
    lights[int(input())] = 1

l = 1
tmp = sum(lights[1:k+1])    # 처음 구역 (1~k까지) 부서진 신호등 다 더하기
answer = tmp
for i in range(k+1, n+1):
    tmp -= lights[l]    # 이전 지점(시작지점) 신호등 빼기
    l += 1  # 옮기기

    tmp += lights[i]    # 끝 지점 신호등 더하기

    if tmp < answer:    # 고칠 신호등 개수 최소로 갱신
        answer = tmp

print(answer)