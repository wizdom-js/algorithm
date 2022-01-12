import sys
sys.stdin = open('input.txt')



def eratos(n):
    for i in range(2, n + 1):
        if i * i > n:
            return

        if not is_prime[i]:
            continue

        for j in range(i*i, n+1, i):
            is_prime[j] = False

n = int(input())
is_prime = [True for _ in range(10001)]
eratos(10000)

p_num1, p_num2 = 2, 3
for i in range(5, n):
    if is_prime[i]:
        if p_num1 * p_num2 <= n:
            p_num1 = p_num2
            p_num2 = i
        else:
            break
print(p_num1 * p_num2)

#     if i * i > n:
#         break
#
#     if is_prime[i] and n % i == 0:
#         p_num2 = n // i
#         if is_prime[p_num2]:
#             p_num1 = i
#             break
#
# for i in range(p_num2+1, n+1):
#     if is_prime[i]:
#         print(i * p_num1)
#         break


