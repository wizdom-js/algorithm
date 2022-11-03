import sys
sys.stdin = open('input.txt')

n = int(input())
numbers = sorted(map(int, input().split()))
# is_good = dict()
#
# answer = 0
# zero_cnt = 0
# for i in range(n):
#     number = numbers[i]
#     if not is_good.get(number):
#         is_good[number] = 0
#
#     if number == 0:
#         zero_cnt += 1
#         if zero_cnt == 2:
#             answer += n - i - 1
#         elif zero_cnt == 3:
#             is_good[0] = 1
#         continue
#
#     for j in range(i+1, n):
#         is_good[number + numbers[j]] = 1
#
# for number in numbers:
#     answer += is_good[number]
#
# print(answer)
answer = 0
for i in range(n):
    target_number = numbers[i]
    l, r = 0, n - 1
    if l == i: l += 1
    if r == i: r -= 1

    while l < r:
        number = numbers[l] + numbers[r]
        if target_number < number:
            r -= 1
            if r == i: r -= 1
        elif target_number > number:
            l += 1
            if l == i: l += 1
        else:
            answer += 1
            break

print(answer)
