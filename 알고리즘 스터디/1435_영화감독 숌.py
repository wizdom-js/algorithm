import sys
sys.stdin = open('input.txt')

n = int(input())

title = ['666']
ok = 0
while ok <= n:
    a = ok // 19
    b = ok % 19

    if b in range(6, 16):
        print(a, 666, b-6)
    elif b in range(16, 19):
        print(a, b%10, 666)
    else:
        print(a, b, 666)

    ok += 1
# ok = 0
# for num in map(str, range(666, 10000000000000000000000)):
#     if '666' in num:
#         ok += 1
#
#     if ok == n:
#         break
# print(num)