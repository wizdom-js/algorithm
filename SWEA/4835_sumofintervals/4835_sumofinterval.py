import sys
sys.stdin = open('input.txt')

# tc 수
tc = int(input())

# tc 수만큼 반복
for idx in range(1, tc+1):
    # 정수의 개수 n, 구간의 개수 M:
    n, m = map(int, input().split())
    # n개의 정수 ai
    numbers = list(map(int, input().split()))

    # 최소 구간, 최대 구간 초기화
    min_ai = 10000000000000000000000000
    max_ai = 0
    # 구간을 구할 것이므로 구간의 개수만큼 뺀 n-m+1 만큼 반복.
    for i in range(n-m+1):
        # section = sum(numbers[i:i + m])
        section = 0
        for j in range(i, i+m):
            section += numbers[j]

        # 최소 구간 판별
        if section < min_ai:
            min_ai = section

        # 최대 구간 판별
        if section > max_ai:
            max_ai = section

    print('#{} {}'.format(idx, max_ai-min_ai))