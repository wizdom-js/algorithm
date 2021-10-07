import sys
sys.stdin = open('input.txt')

def recur(idx, total):
    global answer

    if idx == n:    # 일 배분 다 했다면
        answer = max(answer, total) # 최대 확률로 갱신
        return

    if total <= answer: # 가지치기
        return

    for i in range(n):
        if not visited[i]:  # i 일 배분한적 없다면
            visited[i] = True   # idx 직원이 i 일 해
            recur(idx+1, total*percentage[idx][i]*0.01)   # 다음 직원으로 넘어가
            visited[i] = False  # 다음 사용을 위해 방문 해제


for idx in range(1, int(input())+1):
    n = int(input())
    percentage = [list(map(int, input().split())) for _ in range(n)]

    visited = [False for _ in range(n)] # 방문 처리
    answer = 0
    recur(0, 1)

    print('#{} {:7f}'.format(idx, answer*100))