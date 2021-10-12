import sys
sys.stdin = open('sample_input.txt')


############# 조합 구현 ####################


# 조합 구하기
def combination(idx, cnt, a_arr):
    if cnt == n//2: # 식재료 다 골랐다면
        cal_diff(a_arr) # 두 음식의 맛 차이 구하러 고고
        return

    for i in range(idx, n):
        combination(i+1, cnt+1, a_arr+[i])  # 다음 번호 구해 [0, 1, 2] -> [0, 1, 3] -> [0, 1, 4]


# a, b 음식 맛 차이 구하기
def cal_diff(a_arr):
    global answer

    a, b = 0, 0
    b_arr = [i for i in range(n) if i not in a_arr] # a 음식에서 선택하지 않은 식재료 선택
    for i in range(n//2-1):
        for j in range(i+1, n//2):
            a += synergy[a_arr[i]][a_arr[j]] + synergy[a_arr[j]][a_arr[i]]  # a 음식의 맛 더하기
            b += synergy[b_arr[i]][b_arr[j]] + synergy[b_arr[j]][b_arr[i]]  # b 음식의 맛 더하기

    answer = min(answer, abs(a-b))  # 최소값으로 갱신


tc = int(input())
for idx in range(1, tc+1):
    n = int(input())    # 식재료 개수
    synergy = [list(map(int, input().split())) for _ in range(n)]   # 음식들의 시너지

    answer = 9999999999
    combination(0, 0, [])
    print('#{} {}'.format(idx, answer))
