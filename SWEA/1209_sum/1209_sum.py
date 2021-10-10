import sys
sys.stdin = open('input.txt')

# 10개의 테스트 케이스
for idx in range(1, 11):
    n = int(input())
    # 정사각형 안의 요소들 받아오기
    board = [list(map(int, input().split())) for _ in range(100)]

    diagonal_t = 0 # 대각선 합
    r_diagonal_t = 0 # 반대편 대각선 합
    max_col = 0 # 최대 열의 합
    max_row = 0 # 최대 행의 합
    total = [] # 합들을 담을 리스트

    for i in range(100):
        # 대각선 값 더해주기
        # (대각선의 방향은 상관없지만 그림대로 짜보았다)
        diagonal_t += board[i][i] # 좌상 -> 우하
        r_diagonal_t += board[i][99 - i] # 우상 -> 좌하

        # 매 column 합 담을 변수
        column_t = 0
        for j in range(100):
            # column 더하기
            column_t += board[j][i]

        # 이전의 열 또는 행 보다 크다면 해당 값 저장
        max_col = column_t if column_t > max_col else max_col
        max_row = sum(board[i]) if sum(board[i]) > max_row else max_row

    # 4가지 라인 중, 가장 합이 큰 값 출력
    print('#{} {}'.format(idx, max(max_col, max_row, diagonal_t, r_diagonal_t)))

