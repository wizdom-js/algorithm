import sys
sys.stdin = open('input.txt')

# 소수인지 판별하는 함수
def is_pn(n):
    for i in range(2, n):
        if i * i > n:   # 이 뒤는 볼 필요도 없어
            break

        if n % i == 0:  # 소수가 아니라면 ? False 반환
            return False
    return True

n = int(input())  # 수열의 길이
numbers = set(map(int, input().split())) # 입력받는 수열

answer = 1
for n in numbers:
    if is_pn(n):
        answer *= n

if answer == 1:   # 소수 없어
    print(-1)
else:
    print(answer)