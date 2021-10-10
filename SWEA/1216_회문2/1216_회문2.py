import sys
sys.stdin = open('input.txt')


# 구현은 했으나 아직 인덱스 에러를 해결하지 못했음
# 디버깅 돌려보면서 찾는 중입니다.

def is_palindrome(i, j, k, board):
    len_board_h = len(board)//2

    if len(board) % 2:
        start = board[:len_board_h]  # 구간의 처음 ~ 중간까지의 범위
        end = board[:len_board_h:-1]  # 중간 ~ 구간의 끝 까지의 범위 (비교할 수 있도록 반대로 슬라이싱하였다.)
                                        # [구간의 끝 : 중간 : -1]
    # 회문의 길이가 홀수일 떄
    else:
        start = board[:len_board_h]  # 구간의 처음 ~ 중간 글자 이전
        end = board[:len_board_h-1:-1]  # 중간글자 다음부터 ~ 구간의 끝

    # 비교한 두 범위가 같다면 정답을 반환한다.
    if start == end:
        return board

    return []


for idx in range(1, 11):
    n = int(input())
    board = [list(input()) for _ in range(100)]
    board_r = list(map(list, zip(*board)))

    answer = 1
    for i in range(100):
        for j in range(98):
            for k in range(j+2, 101):

                # 가로
                garo = is_palindrome(i, j, k, board[i][j:k])
                if len(garo) > answer:
                    answer = len(garo)


                # 세로
                sero = is_palindrome(i, j, k, board_r[i][j:k])
                if len(sero) > answer:
                    answer = len(sero)


    print('#{} {}'.format(idx, answer))