import sys
sys.stdin = open('input.txt')

# 1 ~ 12까지의 숫자를 원소로 가진 집합 a
a = list(range(1, 13))
tc = int(input())

for idx in range(1, tc+1):
    # 만족해야하는 부분집합 원소의 수 n, 부분 집합의 합 k
    n, k = map(int, input().split())
    # 조건을 만족하는 부분집합의 개수
    count = 0

    # 모든 부분집합 검사
    for i in range(1<<12):
        subset_n = 0        # 부분집합 원소 개수
        subset_sum = 0      # 부분집합의 합

        # a의 모든 원소를 반복
        for j in range(12):
            # i의 j번째 비트가 1이라면 (찾으려는 부분집합(i)와 현재 인덱스(j) 사이의 교집합이 있다면)
            if i & (1<<j):
                subset_n += 1       # + 원소 개수
                subset_sum += a[j]  # + 원소 값

        # 부분집합의 원소 개수와 합이 각각 n, k라면 count + 1
        if subset_n == n and subset_sum == k:
            count += 1

    print('#{} {}'.format(idx, count))