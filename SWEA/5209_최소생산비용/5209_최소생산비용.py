import sys
sys.stdin = open('sample_input.txt')


def recur(idx, total):
    global answer

    if idx == n:    # 공장 다 돌았다면
        answer = min(answer, total) # 최소비용으로 갱신
        return

    if answer <= total:  # 이미 저장되어있는 생산비용보다 크다면 멈춰
        return

    for i in range(n):
        if not visited[i]:  # i 공장에서 생산한적 없다면
            visited[i] = True   # 생산해
            recur(idx+1, total+costs[idx][i])   # 다음공장 ㄱ
            visited[i] = False  # 다음 사용을 위해 방문 해제


for idx in range(1, int(input())+1):
    n = int(input())    # 제품 수
    costs = [list(map(int, input().split())) for _ in range(n)] # 공장별 생산비용
    visited = [False for _ in range(n)] # 해당 공장에서 생산한 적 있는지 방문 처리

    answer = 9999999999999

    recur(0, 0)
    print('#{} {}'.format(idx, answer))