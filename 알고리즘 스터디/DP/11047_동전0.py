import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())    # 동전 종류 수 n, 만들 가치의 합 k
coins = [int(input()) for _ in range(n)]
cnt = 0  # 총 사용한 동전 개수

for i in range(n-1, -1, -1):    # 큰수부터 시작
    if k < coins[i]:    # k보다 동전이 크면 pass
        continue

    # 동전이 k보다 작은 경우
    temp = k // coins[i]    # i번째의 동전으로 만들 수 있는 최대 수
    k -= coins[i] * temp    # i번째의 동전으로 만들 수 있는 가치만큼 빼준다.

    cnt += temp # 방금 사용한 동전 수를 cnt에 합쳐준다.
    if not k:   # k가 0이 되면 중단
        break

print(cnt)