import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# s, e = 0, 1
# answer = 0

######## 풀이 1 (sum 활) ######
# while e <= n and s <= e:
#     tmp = sum(numbers[s:e])   # 합 구하기
#
#     if tmp == m:      # 목표 한 수라면
#         answer += 1
#         e += 1    # e 포인터 옮기기
#     elif tmp > m:     # 목표한 수보다 크다면
#         s += 1    # s 포인터 옮기기
#     else:             # 목표한 수보다 작다면
#         e += 1    # e 포인터 옮기기
#
# print(answer)


######## 풀이 2 (sum 활용 X) ######
s, e = 0, 0
answer = 0
tmp = 0
while e <= n and s <= e:
    if tmp == m:
        answer += 1
    elif tmp > m:
        tmp -= numbers[s]
        s += 1
        continue

    if e == n: break
    tmp += numbers[e]
    e += 1
print(answer)


######## 풀이 3 (for문으로 s 고정) ######
# tmp = 0
# for s in range(n):
#     while tmp < m and e < n:
#         tmp += numbers[e]
#         e += 1
#     if tmp == m:
#         answer += 1
#     tmp -= numbers[s]
#
# print(answer)