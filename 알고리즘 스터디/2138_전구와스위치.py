import sys
sys.stdin = open('input.txt')

# def onoff(cnt, now):
#     for i in range(1, n):
#         if target[i-1] != now[i-1]:
#             cnt += 1
#             now[i-1] =  target[i-1]
#             now[i] = 0 if now[i] else 1
#             if i != n-1:
#                 now[i+1] = 0 if now[i+1] else 1
#
#     return cnt if now == target else -1
#
# n = int(input())
# now1 = list(map(int, input()))
# target = list(map(int, input()))
#
# now2 = now1[:]
# for i in range(2):
#     now2[i] = 0 if now1[i] else 1
#
# try1 = onoff(0, now1)
# try2 = onoff(1, now2)
#
# if try1 != -1 and try2 != -1:
#     answer = try1 if try1 < try2 else try2
# elif try1 == -1 or try2 == -1:
#     answer = try1 if try1 > try2 else try2
# else:
#     answer = -1
#
# print(answer)


# 영남이 오빠 도움 추가 버전
def onoff(cnt, now):
    for i in range(1, n):
        if target[i-1] != now[i-1]:
            cnt += 1
            now[i-1] = target[i-1]
            now[i] = 0 if now[i] else 1
            if i != n-1:
                now[i+1] = 0 if now[i+1] else 1
    return cnt


n = int(input())
now1 = list(map(int, input()))
target = list(map(int, input()))

now2 = now1[:]
for i in range(2):
    now2[i] = 0 if now1[i] else 1

try1 = onoff(0, now1)
if now1 == target:
    print(try1)
    exit()

try2 = onoff(1, now2)
if now2 == target:
    print(try2)
    exit()

print(-1)