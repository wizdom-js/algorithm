import sys
sys.stdin = open('sample_input.txt')


def recur(cnt, now, total): #(횟수, 현재위치, 현재까지 배터리 소비량)
    global answer
    if cnt == n:    # n회차이면 끝
        total += arr[now][0]    # 마지막 사무실에 돌아오는 소비량 더해주기
        if total < answer:  # 총 소비량이 answer에 있는 값보다 작다면 갱신
            answer = total
            return

    if answer < total:  # 이미 소비량 answer보다 크다면 돌아가
        return

    for next in range(1, n):
        # arr[i][i] 이면 해당 값은 0이므로, now 와 next가 같지않고, 방문한 곳이 아니라면
        if now != next and not visited[next]:
            visited[next] = True    # 방문처리
            recur(cnt+1, next, total + arr[now][next])  # 들어가
            visited[next] = False   # 다음 사용을 위해 방문 풀어주기


tc = int(input())
for idx in range(1, tc+1):
    n = int(input())    # 관리구역 번호
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False for _ in range(n)] # 방문처리 리스트

    answer = 99999999999999999999   # 최소 배터리 소비량 받을 변수
    recur(1, 0, 0)

    print('#{} {}'.format(idx, answer))