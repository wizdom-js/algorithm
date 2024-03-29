import sys
sys.stdin = open('sample_input.txt')

from itertools import combinations  ######### combinations 사용 #########


tc = int(input())
for idx in range(1, tc+1):
    n = int(input())    # 식재료 개수
    synergy = [list(map(int, input().split())) for _ in range(n)]   # 음식들의 시너지

    answer = 9999999999
    for a_arr in combinations(range(n), n//2):  # a 음식 고를 식재료 선택
        b_arr = [i for i in range(n) if i not in a_arr]  # a 음식에서 선택하지 않은 식재료 선택
        a, b = 0, 0
        for i in range(n // 2 - 1):
            for j in range(i + 1, n // 2):
                a += synergy[a_arr[i]][a_arr[j]] + synergy[a_arr[j]][a_arr[i]]  # a 음식의 맛 더하기
                b += synergy[b_arr[i]][b_arr[j]] + synergy[b_arr[j]][b_arr[i]]  # b 음식의 맛 더하기

        answer = min(answer, abs(a - b))  # 최소값으로 갱신

    print('#{} {}'.format(idx, answer))
