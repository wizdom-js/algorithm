def solution(board, skill):
    h = len(board)
    w = len(board[0])

    tmp = [[0 for _ in range(w + 1)] for _ in range(h + 1)]  # 누적합 기록 배열
    for typ, r1, c1, r2, c2, degree in skill:
        if typ == 1:  # 공격 받은 경우 => 부호 반대로
            degree *= -1
        # 누적합 기록하기
        tmp[r1][c1] += degree
        tmp[r1][c2 + 1] += -degree
        tmp[r2 + 1][c1] += -degree
        tmp[r2 + 1][c2 + 1] += degree

    # 행 누적합
    for y in range(h):
        for x in range(w):
            tmp[y][x + 1] += tmp[y][x]

    # 열 누적합
    for y in range(h):
        for x in range(w):
            tmp[y + 1][x] += tmp[y][x]

    answer = 0
    # 기존 내구도랑 합치기
    for y in range(h):
        for x in range(w):
            board[y][x] += tmp[y][x]
            # 내구도가 1 이상이면 정답 +1
            if board[y][x] > 0:
                answer += 1

    [i+1][j+1] = [i][j+1] + [i+1][j] - [i][j] - ekfmsrj[i][j]

    return answer