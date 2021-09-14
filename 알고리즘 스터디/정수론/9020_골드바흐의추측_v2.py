import sys
sys.stdin = open('input.txt')

# 에라토스테네스의 채로 소수인지 판별 해놓기
is_prime = [True for _ in range(10001)]
for i in range(2, 10001):
    if i*i > 10000:
        break
    if not is_prime[i]:
        continue
    for j in range(i*i, 10001, i):
        is_prime[j] = False

tc = int(input())
for _ in range(tc):
    N = int(input())

    s = N//2    # 반으로 쪼개기
    e = N//2
    # 같은 수 두번 더했는데 답인 경우
    if is_prime[N//2]:
        if s + e == N:
            print(s, e)
    else:
        # 포인트 두개로 한칸씩 옮겨주며 답을 찾는다. 왜냐면 중간에서 같은 차이만큼 떨어져 있기 때문
        while True:
            s -= 1
            e += 1
            if is_prime[s] and is_prime[e]:
                print(s, e)
                break







