import sys
sys.stdin = open('input.txt')

# (인덱스, 난쟁이 선택 수, 더한 무게, 난쟁이 배열)
# def dfs(i, n, w, arr):
#     global answer
#
#     # 난쟁이들의 무게의 합이 100이고 7명이라면 정답 반환
#     if w == 100 and n == 7:
#         answer = arr
#         return
#
#     # 이미 정답 발견 했거나, 무게가 100이상이거나, 난쟁이 수가 7명이거나, 인덱스 초과라면 돌아가
#     if answer or w > 100 or n == 7 or i == 9:
#         return
#
#     dfs(i+1, n+1, w + dwarfs[i], arr+[dwarfs[i]])   # i번째 난쟁이 선택
#     dfs(i+1, n, w, arr)     # i번째 난쟁이 선택 X
#
#
# dwarfs = sorted([int(input()) for _ in range(9)])
# answer = []
# dfs(0, 0, 0, [])
#
# for i in answer:
#     print(i)


############################################################


# (인덱스, 난쟁이 선택 수, 더한 무게, 난쟁이 배열)
def dfs(i, n, w):

    # 난쟁이들의 무게의 합이 100이고 7명이라면 정답 출력
    if w == 100 and n == 7:
        for i in answer:
            print(i)
        exit() # 답이 여러개라도 하나의 케이스만 출력해야 하므로 걍 종료
        return

    # 무게가 100이상이거나, 난쟁이 수가 7명이거나, 인덱스 초과라면 돌아가
    if w > 100 or n == 7 or i == 9:
        return

    answer.append(dwarfs[i])
    dfs(i+1, n+1, w + dwarfs[i])   # i번째 난쟁이 선택
    answer.pop()
    dfs(i+1, n, w)     # i번째 난쟁이 선택 X


dwarfs = sorted([int(input()) for _ in range(9)])
answer = []
dfs(0, 0, 0)

