import sys
sys.stdin = open('sample_input.txt')

# 문자열 같은지 같지 않은지 비교
def search(i, j, board):
    # 회문의 길이가 홀수일 때랑 짝수일 때 슬라이싱의 범위가 다르므로 조건문 설정
    # 회문의 길이가 짝수일 때
    if m % 2:
        start = board[:m_half]          # 구간의 처음 ~ 중간까지의 범위
        end = board[:m_half:-1]     # 중간 ~ 구간의 끝 까지의 범위 (비교할 수 있도록 반대로 슬라이싱하였다.)
                                                # [구간의 끝 : 중간 : -1]
    # 회문의 길이가 홀수일 떄
    else:
        start = board[:m_half]          # 구간의 처음 ~ 중간 글자 이전
        end = board[:m_half-1:-1]   # 중간글자 다음부터 ~ 구간의 끝

    # 비교한 두 범위가 같다면 정답을 반환한다.
    if start == end:
        return board

    return 0


tc = int(input())

for idx in range(1, tc+1):
    # 글자판 크기 n, 회문의 길이 m
    n, m = map(int, input().split())
    # 글자판 받아오기
    board = [list(input()) for _ in range(n)]
    # 글자판 뒤집기
    # board안의 1차원 리스트를 다 가져와서, 인덱스 순서에 맞는 각 원소들을 하나의 리스트로 묶어 반환한다. (여기서 다시 감싸면 2차원이됨)
    board_r = list(map(list, zip(*board)))


    m_half = m // 2     # m의 길이 절반 구하기 (반만 비교하면 되니까)
    answer = None       # 정답이 들어갈 변수
    for i in range(n):
        # 회문의 길이가 정해져 있으므로 회문의 구간을 한칸씩 옮겼을 때
        # 글자판의 끝까지만 for문을 돈다.
        for j in range(n-m+1):

            # 가로
            garo = search(i, j, board[i][j:m+j])
            # 정답이 반환됐다면 문자열로 변환 후 반복문 중단.
            if garo:
                answer = ''.join(garo)
                break

            # 세로
            sero = search(i, j, board_r[i][j:m+j])
            if sero:
                answer = ''.join(sero)
                break

        # 정답을 찾았다면 반복문을 돌 필요 X -> 중단
        if answer:
            break

    print('#{} {}'.format(idx, answer))
