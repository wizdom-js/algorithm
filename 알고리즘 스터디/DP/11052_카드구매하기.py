import sys
sys.stdin = open('input.txt')

n = int(input())
cards = list(map(int, input().split()))
answer = 0

for i in range(1, n+1):
    if n % i:  # i개로 n개의 카드를 채울 수 없을 때
        temp = cards[i-1] * (n//i) + cards[(n%i)-1]   # i개의 카드팩으로 n을 채우고, 남는건 그만큼에 해당하는 개수의 카드팩 사
    else:   # i개로 n개의 카드 다 채울 때
        temp = cards[i-1] * (n//i)  # i개 들어있는 카드팩 n//i개만큼 사기

    answer = max(answer, temp)  # 금액의 최댓값 갱신

print(answer)


#################################################


n = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]    # 각 자리에는 카드 i개를 구매하는 최대 가격이 저장됨

for i in range(1, n+1):
   for j in range(1, i+1): # i가 4면 (3, 1), (2, 2), (1, 3)일 때를 보는것
       dp[i] = max(dp[i-j] + cards[j], dp[i]) # i개 구매할때의 최대 가격 갱신

print(dp[n])

'''
4
1 5 6 7
5
10 9 8 7 6
10
1 1 2 3 5 8 13 21 34 55
10
5 10 11 12 13 30 35 40 45 47
4
5 2 8 10
4
3 5 15 16
7
742 3302 5186 6619 567 5068 8591
12
1 1 6 8 11 1 1 1 1 1 1 1
6
1 5 6 1 1 1
7
1 2 0 4 1 1 1
'''