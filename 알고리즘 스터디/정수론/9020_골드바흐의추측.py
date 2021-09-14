import sys
sys.stdin = open('input.txt')

## 시간초과

# 소수인지 판별
def is_pn(n):
    for i in range(2, n):
        if i * i > n:
            return True
        if n % i == 0:
            return False
    return True


tc = int(input())
for _ in range(tc):
    N = int(input())

    prime_n = []
    answer = False
    for n in range(2, N):
        if is_pn(n):    # 소수인가요 ?
            if 2*n == N:    # 자신과 자신을 더하면 N이 되나요?
                print(n, n) # 바로 출력하고
                answer = True   # 뒤의 코드 볼 필요없이 끝내기
                break
            else:
                prime_n.append(n)   # 그렇지 않다면 추가

    # 아직 답 못찾은 경우
    if not answer:
        ans1, ans2 = 0, 99999999    # 초기화
        for i in range(len(prime_n)-1):
            for j in range(i, len(prime_n)):
                if prime_n[i] + prime_n[j] == N: # 소수 두개를 더하여 N이 되는 경우
                    n1, n2 = prime_n[i], prime_n[j]
                    if n2-n1 < ans2-ans1:   # 차이가 기존보다 더 작으면 갱신
                        ans1 = n1
                        ans2 = n2
        print(n1, n2)   # 최종 소수 두개 출력
