import sys
sys.stdin = open('sample_input.txt')

from itertools import permutations, combinations  ######### permutations, combinations 사용 #########


tc = int(input())
for idx in range(1, tc+1):
    n = int(input())    # 식재료 개수
    synergy = [list(map(int, input().split())) for _ in range(n)]   # 음식들의 시너지

    answer = 9999999999
    for a_arr in combinations(range(n), n//2):  # a 음식 고를 식재료 선택
        b_arr = [i for i in range(n) if i not in a_arr]  # a 음식에서 선택하지 않은 식재료 선택
        a, b = 0, 0
        for i, j in permutations(a_arr, 2):
            a += synergy[i][j]   # a 음식의 맛 더하기

        for i, j in permutations(b_arr, 2):
            b += synergy[i][j]   # b 음식의 맛 더하기

        answer = min(answer, abs(a - b))  # 최소값으로 갱신

    print('#{} {}'.format(idx, answer))
