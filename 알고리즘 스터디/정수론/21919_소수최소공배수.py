import sys
sys.stdin = open('input.txt')

########## 최소 공배수 템플릿 쓴거 ########3

# 소수인지 판별하는 함수
def is_pn(n):
    for i in range(2, n):
        if i * i > n:   # 이 뒤는 볼 필요도 없어
            break

        if n % i == 0:  # 소수가 아니라면 ? False 반환
            return False
    return True

# 최소 공배수 함수
def lcm(num1, num2):
    n1 = num1
    n2 = num2
    while n1 % n2 != 0:
        n1, n2 = n2, n1 % n2
    return num1 * num2 // n2


n = int(input())  # 수열의 길이
numbers = list(map(int, input().split())) # 입력받는 수열

# 소수인 수만 모으자
prime_number = []
for n in numbers:
    if is_pn(n):
        prime_number.append(n)

if not prime_number:   # 소수 없어
    print(-1)
elif len(prime_number) == 1: # 소수 한개야
    print(prime_number[0])
else:   # 소수 두개 이상
    n1 = prime_number[0]
    for n in prime_number[1:]:
        n1 = lcm(n1, n)
    print(n1)   # 최소 공배수 출력