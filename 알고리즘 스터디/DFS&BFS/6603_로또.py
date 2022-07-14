import sys
sys.stdin = open('input.txt')

# 모든 경우를 구할 때 dfs

# 조합 구현
def dfs(s, depth):
    if depth == 6:  # 로또 6개 골랐다면 출력
        print(*combination)
        return

    for i in range(s, k):   # 중복 방지위해 s부터 시작 k개 까지
        combination[depth] = numbers[i] # 해당 깊이 자리에 k개의 숫자 중, 고른 번호 넣기
        dfs(i+1, depth+1)   # 다음 번호 고르러 가기


combination = [0 for _ in range(6)] # 고른 번호가 들어갈 리스트

while True:
    test_case = list(map(int, input().split()))
    if test_case[0] == 0:   # 입력의 마지막 줄이라면
        break

    k = test_case[0]    # 고른 수의 개수
    numbers = test_case[1:] # 숫자들

    dfs(0, 0)
    print()