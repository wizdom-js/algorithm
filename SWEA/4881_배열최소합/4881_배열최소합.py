import sys
sys.stdin = open("sample_input.txt")

# 배열 선택 함수 (진행할 행, 이전까지의 선택 숫자들의 합)
def select(y, temp_sum):

    global min_sum

    # 행의 맨 마지막까지 갔을 경우 (더이상 갈 곳 없으면)
    if y == n:
        # 만약 여태 더한 값이 min_sum에 저장되어 있는 값보다 작다면 갱신하고 돌아가기
        if temp_sum < min_sum:
            min_sum = temp_sum
        return

    # 여태 더한 값이 이미 min_sum에 저장되어있는 값보다 크다면 들어갈 필요 없어 돌아가
    if min_sum <= temp_sum:
        return

    for i in range(n):
        # 방문 안한 열 이라면 (겹치지 않는다면)
        if not visited[i]:
            visited[i] = 1  # 방문처리
            select(y+1, temp_sum + board[y][i]) # 다음 행으로 들어가기 그리고 숫자 더해주기
            visited[i] = 0  # 다음 사용을 위해 원상복구



tc = int(input())

for idx in range(1, tc+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    # 방문처리 해줄 리스트
    visited = [0 for _ in range(n)]

    # 최소 합 담을 변수 (대각선의 합으로 넣어주었다.)
    min_sum = sum([board[i][i] for i in range(n)])

    # 함수 실행
    select(0, 0)

    print('#{} {}'.format(idx, min_sum))


