import sys
sys.stdin = open('input.txt')

# TC 수
tc = int(input())

# tc 수만큼 반복
for idx in range(1, tc+1):
    # 양수의 개수 N
    n = int(input())
    # N개의 양수 numbers
    numbers = list(map(int, input().split()))

    min_num = max_num = numbers[0]
    for i in range(1, n):
        # min 구하기
        if min_num > numbers[i]:
            min_num = numbers[i]

        # max 구하기
        if max_num < numbers[i]:
            max_num = numbers[i]


    print('#{} {}'.format(idx, max_num-min_num))