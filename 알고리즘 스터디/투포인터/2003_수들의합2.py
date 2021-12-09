import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# s, e = 0, 1
# answer = 0

######## 풀이 1 ######
# while e <= n and s <= e:
#     tmp = sum(numbers[s:e])
#
#     if tmp == m:
#         answer += 1
#         e += 1
#     elif tmp > m:
#         s += 1
#     else:
#         e += 1
#
# print(answer)


######## 풀이 2 ######
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


######## 풀이 3 ######
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