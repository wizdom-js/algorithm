import sys
sys.stdin = open('input.txt')

# n = int(input())
# numbers = list(map(int, input().split()))
# sorted_n = sorted(numbers)
#
# l = 0
# r = 2
# ok = False
# while True:
#     if numbers[r] < numbers[l]:
#         numbers[l], numbers[r] = numbers[r], numbers[l]
#         ok = True
#     if r == n-1:
#         if ok:
#             l = 0
#             r = 2
#             ok = False
#             continue
#         else:
#             break
#     l += 1
#     r += 1
#
# if numbers == sorted_n:
#     print('YES')
# else:
#     print('NO')
#     print(sorted_n)
#     print(numbers)


n = int(input())
numbers = list(enumerate(map(int, input().split())))
print(numbers)
numbers.sort(key=lambda x: x[1])
print(numbers)

is_even = True
for idx, num in numbers:
    if (idx % 2 and is_even) or (not idx % 2 and not is_even): # 홀수, 짝수
        print('NO')
        break

    is_even = not is_even

else:
    print('YES')


n = int(input())
numbers = list(map(int, input().split()))
for i in range(n):
    if i % 2:
        if numbers[i] % 2:
            print('NO')
            exit()
else:
    print('YES')