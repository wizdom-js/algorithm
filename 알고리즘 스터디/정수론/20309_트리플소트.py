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
numbers = list(enumerate(map(int, input().split())))   # (인덱스, 숫자) 같이 저장
print(numbers)
numbers.sort(key=lambda x: x[1])    # 숫자 기준으로 정렬
print(numbers)

is_even = True  # 홀수 순서, 짝수 순서 판별
for idx, num in numbers:
    if (idx % 2 and is_even) or (not idx % 2 and not is_even): # 인덱스가 홀수인데 짝수 순서이거나, 인덱스가 짝수인데 홀수 순서라면
        print('NO') # 정렬 불가능
        break

    is_even = not is_even

else:
    print('YES')


n = int(input())    # 배열의 크기
numbers = list(map(int, input().split()))   # 배열의 원소
for i in range(n):
    # 짝수번째 값이 모두 짝수여야 정렬 가능
    if i % 2:   # 짝수 자리라면 (0부터 시작하므로 사실상 짝수 자리)
        if numbers[i] % 2:  # 근데 원소가 홀수라면
            print('NO') # 정렬 불가능
            exit()
else:
    print('YES')    # 그 외는 정렬 가능